import copy
import pathlib
from typing import Any, Dict, List, Optional, Union

from anyscale._private.anyscale_client import (
    AnyscaleClient,
    AnyscaleClientInterface,
    WORKSPACE_CLUSTER_NAME_PREFIX,
)
from anyscale.cli_logger import BlockLogger
from anyscale.client.openapi_client.models import (
    ComputeTemplateConfig,
    DecoratedComputeTemplateConfig,
)
from anyscale.sdk.anyscale_client.models import (
    AccessConfig,
    ApplyServiceModel,
    ProductionServiceV2VersionModel,
    RayGCSExternalStorageConfig,
    ServiceConfig as ExternalAPIServiceConfig,
    ServiceEventCurrentState,
    ServiceModel,
)
from anyscale.service.models import (
    ServiceConfig,
    ServiceState,
    ServiceStatus,
    ServiceVersionStatus,
)
from anyscale.utils.runtime_env import is_dir_remote_uri, parse_requirements_file
from anyscale.utils.workspace_notification import (
    WorkspaceNotification,
    WorkspaceNotificationAction,
)


logger = BlockLogger()


class ServiceSDK:
    def __init__(self, *, client: Optional[AnyscaleClientInterface] = None):
        self._client = client or AnyscaleClient()

    def _override_and_load_requirements_files(
        self, config: ServiceConfig, *, autopopulate_in_workspace: bool = True
    ) -> ServiceConfig:
        """Replaces any pip fields in runtime_envs with their parsed file contents.

        If autopopulate_from_workspace is passed and this code is running inside a
        workspace, any applications that do not have a "pip" or "conda" field
        specified in the runtime_env will have it autopopulated with the
        workspace-tracked dependencies.
        """
        new_applications = copy.deepcopy(config.applications)

        local_path_to_parsed_requirements: Dict[str, List[str]] = {}

        def _load_requirements_file_memoized(
            target: Union[str, List[str]]
        ) -> List[str]:
            if isinstance(target, list):
                return target
            elif target in local_path_to_parsed_requirements:
                return local_path_to_parsed_requirements[target]
            elif isinstance(target, str):
                parsed_requirements = parse_requirements_file(target)
                if parsed_requirements is None:
                    raise FileNotFoundError(
                        f"Requirements file {target} does not exist."
                    )
                local_path_to_parsed_requirements[target] = parsed_requirements
                return parsed_requirements
            else:
                raise TypeError("pip field in runtime_env must be a list or string.")

            return parsed_requirements

        for application in new_applications:
            runtime_env = application.get("runtime_env", {})
            if "pip" in runtime_env:
                # Allow `None` to be used as a signal not to override.
                if runtime_env["pip"] is not None:
                    # If the user passed a "pip" field, load from the file if necessary.
                    runtime_env["pip"] = _load_requirements_file_memoized(
                        runtime_env["pip"]
                    )
            elif (
                "conda" not in runtime_env
                and autopopulate_in_workspace
                and self._client.inside_workspace()
            ):
                # If no "pip" or "conda" field was specified, try filling it in from
                # the workspace-tracked requirements file.
                workspace_requirements_path = (
                    self._client.get_workspace_requirements_path()
                )
                if workspace_requirements_path is not None:
                    logger.info("Including workspace-managed pip dependencies.")
                    runtime_env["pip"] = _load_requirements_file_memoized(
                        self._client.get_workspace_requirements_path()
                    )

        return config.options(applications=new_applications)

    def _override_and_upload_local_dirs(
        self,
        config: ServiceConfig,
        *,
        autopopulate_in_workspace: bool = True,
        cloud_id: Optional[str] = None,
    ) -> ServiceConfig:
        """Returns a copy of the config with all local dirs converted to remote URIs.

        Local dirs can be specified in the working_dir or py_modules fields of the runtime_env.

        Each unique local directory across these fields will be uploaded once to cloud storage,
        then all occurrences of it in the config will be replaced with the corresponding remote URI.
        """
        new_applications = copy.deepcopy(config.applications)

        local_path_to_uri: Dict[str, str] = {}

        def _upload_dir_memoized(target: str, *, excludes: Optional[List[str]]) -> str:
            if is_dir_remote_uri(target):
                return target
            if target in local_path_to_uri:
                return local_path_to_uri[target]

            logger.info(f"Uploading local dir '{target}' to cloud storage.")
            uri = self._client.upload_local_dir_to_cloud_storage(
                target, cloud_id=cloud_id, excludes=excludes,
            )
            local_path_to_uri[target] = uri
            return uri

        for application in new_applications:
            runtime_env = application.get("runtime_env", {})
            excludes = runtime_env.pop("excludes", None)
            if "working_dir" in runtime_env:
                # Allow `None` to be used as a signal not to override.
                if runtime_env["working_dir"] is not None:
                    runtime_env["working_dir"] = _upload_dir_memoized(
                        runtime_env["working_dir"], excludes=excludes
                    )
            elif autopopulate_in_workspace and self._client.inside_workspace():
                runtime_env["working_dir"] = _upload_dir_memoized(
                    ".", excludes=excludes,
                )

            py_modules = runtime_env.get("py_modules", None)
            if py_modules is not None:
                new_py_modules = []
                for py_module in py_modules:
                    new_py_modules.append(
                        _upload_dir_memoized(py_module, excludes=excludes)
                    )

                application["runtime_env"]["py_modules"] = new_py_modules

            if runtime_env:
                application["runtime_env"] = runtime_env

        return config.options(applications=new_applications)

    def _resolve_compute_config_to_id(
        self, compute_config: Optional[Union[str, Dict]]
    ) -> str:
        if compute_config is None:
            compute_config_id = self._client.get_compute_config_id()
            assert compute_config_id is not None
        elif isinstance(compute_config, str):
            compute_config_id = self._client.get_compute_config_id(
                compute_config_name=compute_config,
            )
            if compute_config_id is None:
                raise ValueError(
                    f"The compute config '{compute_config}' does not exist."
                )
        else:
            try:
                compute_config_template = ComputeTemplateConfig(**compute_config)
            except (ValueError, TypeError) as e:
                raise RuntimeError(f"Invalid compute config: {e}.")

            compute_config_id = self._client.create_anonymous_compute_config(
                compute_config_template
            )

        return compute_config_id

    def _get_default_name(self) -> Optional[str]:
        """Get a default name for the service.

        A default is currently only generated when running inside a workspace
        (from the workspace cluster name), so this function errors if called outside
        a workspace.
        """
        if not self._client.inside_workspace():
            raise ValueError(
                "A service name must be provided when running outside of a workspace."
            )

        name = self._client.get_current_workspace_cluster().name
        # Defensively default to the workspace cluster name as-is if it doesn't
        # start with the expected prefix.
        if name.startswith(WORKSPACE_CLUSTER_NAME_PREFIX):
            name = name[len(WORKSPACE_CLUSTER_NAME_PREFIX) :]

        logger.info(f"No name was specified, using default: '{name}'.")
        return name

    def _get_containerfile_contents(self, path: str) -> str:
        containerfile_path = pathlib.Path(path)
        if not containerfile_path.exists():
            raise FileNotFoundError(
                f"Containerfile '{containerfile_path}' does not exist."
            )
        if not containerfile_path.is_file():
            raise ValueError(f"Containerfile '{containerfile_path}' must be a file.")
        return containerfile_path.read_text()

    def deploy(  # noqa: PLR0912
        self,
        config: ServiceConfig,
        *,
        in_place: bool = False,
        canary_percent: Optional[int] = None,
        max_surge_percent: Optional[int] = None,
    ):
        if not isinstance(in_place, bool):
            raise TypeError("in_place must be a bool.")

        if canary_percent is not None:
            if not isinstance(canary_percent, int):
                raise TypeError("canary_percent must be an int.")
            if canary_percent < 0 or canary_percent > 100:
                raise ValueError("canary_percent must be between 0 and 100.")

        if max_surge_percent is not None:
            if not isinstance(max_surge_percent, int):
                raise TypeError("max_surge_percent must be an int.")

            if max_surge_percent < 0 or max_surge_percent > 100:
                raise ValueError("max_surge_percent must be between 0 and 100.")

        name = config.name or self._get_default_name()

        if config.containerfile is not None:
            build_id = self._client.get_cluster_env_build_id_from_containerfile(
                cluster_env_name=f"image-for-{name}",
                containerfile=self._get_containerfile_contents(config.containerfile),
            )
        elif config.image_uri is not None:
            build_id = self._client.get_cluster_env_build_id(
                image_uri=config.image_uri,
            )
        else:
            build_id = self._client.get_default_build_id()

        compute_config_id = self._resolve_compute_config_to_id(config.compute_config)

        # If a compute config was specified, we need to make sure to used the correct
        # cloud_id when uploading local directories.
        cloud_id = self._client.get_cloud_id(
            compute_config_id=None
            if config.compute_config is None
            else compute_config_id
        )
        config = self._override_and_upload_local_dirs(config, cloud_id=cloud_id)
        config = self._override_and_load_requirements_files(config)

        ray_serve_config: Dict[str, Any] = {"applications": config.applications}
        if config.http_options:
            ray_serve_config["http_options"] = config.http_options
        if config.grpc_options:
            ray_serve_config["grpc_options"] = config.grpc_options

        ray_gcs_external_storage_config = None
        if config.ray_gcs_external_storage_config is not None:
            ray_gcs_external_storage_config = RayGCSExternalStorageConfig(
                **config.ray_gcs_external_storage_config
            )

        service: ServiceModel = self._client.rollout_service(
            ApplyServiceModel(
                name=name,
                project_id=self._client.get_project_id(),
                ray_serve_config=ray_serve_config,
                build_id=build_id,
                compute_config_id=compute_config_id,
                canary_percent=canary_percent,
                max_surge_percent=max_surge_percent,
                rollout_strategy="IN_PLACE" if in_place else "ROLLOUT",
                config=ExternalAPIServiceConfig(
                    access=AccessConfig(
                        use_bearer_token=config.query_auth_token_enabled
                    ),
                ),
                ray_gcs_external_storage_config=ray_gcs_external_storage_config,
            )
        )

        canary_percent_info = (
            ""
            if canary_percent is None
            else f" (target canary percent: {canary_percent})"
        )
        message = f"Service '{name}' deployed{canary_percent_info}."
        logger.info(message)
        if self._client.inside_workspace():
            self._client.send_workspace_notification(
                WorkspaceNotification(
                    body=message,
                    action=WorkspaceNotificationAction(
                        type="navigate-service", title="View Service", value=service.id,
                    ),
                ),
            )
        else:
            # NOTE(edoakes): this link does not currently work for AIOA clouds.
            logger.info(
                f"View the service in the UI: {self._client.get_service_ui_url(service.id)}"
            )

        logger.info(
            "Query the service once it's running using the following curl command:"
        )
        auth_token_header = (
            ""
            if service.auth_token is None
            else f"-H 'Authorization: Bearer {service.auth_token}' "
        )
        logger.info(f"curl {auth_token_header}{service.base_url}/")

    def rollback(
        self, name: Optional[str] = None, *, max_surge_percent: Optional[int] = None,
    ):
        if name is None:
            name = self._get_default_name()

        model: Optional[ServiceModel] = self._client.get_service(name)
        if model is None:
            raise RuntimeError(f"Service with name '{name}' was not found.")

        return self._client.rollback_service(
            model.id, max_surge_percent=max_surge_percent,
        )

    def terminate(self, name: Optional[str] = None):
        if name is None:
            name = self._get_default_name()

        model: Optional[ServiceModel] = self._client.get_service(name)
        if model is None:
            raise RuntimeError(f"Service with name '{name}' was not found.")

        return self._client.terminate_service(model.id,)

    def _strip_none_values_from_dict(self, d: Dict) -> Dict:
        """Return a copy of the dictionary without any keys whose values are None.

        Recursively calls into any dictionary values.
        """
        result = {}
        for k, v in d.items():
            if isinstance(v, dict):
                result[k] = self._strip_none_values_from_dict(v)
            elif v is not None:
                result[k] = v

        return result

    def _get_compute_config_for_status(
        self, compute_config_id: str,
    ) -> Union[str, Dict]:
        """Get the compute config to be displayed in the status for this ID.

        If the compute config refers to an anonymous compute config, its config
        will be returned. Else the name of the compute config will be returned.
        """
        compute_config = self._client.get_compute_config(compute_config_id)
        if compute_config is None:
            raise RuntimeError(
                f"Failed to get compute config for ID {compute_config_id}."
            )

        if not compute_config.anonymous:
            compute_config_name = compute_config.name
            if compute_config.version is not None:
                compute_config_name += f":{compute_config.version}"
            return compute_config_name

        config: DecoratedComputeTemplateConfig = compute_config.config
        config_dict = {
            # Strip some internal fields that we don't want to expose to the user.
            # TODO(edoakes): we should improve the compute config model and avoid this.
            k: v
            for k, v in config.to_dict().items()
            if k
            not in {
                "cloud",
                "cloud_id",
                "maximum_uptime_minutes",
                "idle_termination_minutes",
            }
        }
        return self._strip_none_values_from_dict(config_dict)

    def _service_version_model_to_status(
        self,
        model: ProductionServiceV2VersionModel,
        *,
        service_name: str,
        query_auth_token_enabled: bool,
    ) -> ServiceVersionStatus:
        image_uri = self._client.get_cluster_env_build_image_uri(model.build_id)
        if image_uri is None:
            raise RuntimeError(f"Failed to get image URI for ID {model.build_id}.")

        ray_gcs_external_storage_config = None
        if model.ray_gcs_external_storage_config is not None:
            ray_gcs_external_storage_config = self._strip_none_values_from_dict(
                model.ray_gcs_external_storage_config.to_dict()
            )

        return ServiceVersionStatus(
            name=model.version,
            # NOTE(edoakes): there is also a "current_weight" field but it does not match the UI.
            weight=model.weight,
            config=ServiceConfig(
                name=service_name,
                applications=model.ray_serve_config["applications"],
                image_uri=image_uri,
                compute_config=self._get_compute_config_for_status(
                    model.compute_config_id
                ),
                query_auth_token_enabled=query_auth_token_enabled,
                http_options=model.ray_serve_config.get("http_options", None),
                grpc_options=model.ray_serve_config.get("grpc_options", None),
                ray_gcs_external_storage_config=ray_gcs_external_storage_config,
            ),
        )

    def _service_model_to_status(self, model: ServiceModel) -> ServiceStatus:
        # TODO(edoakes): for some reason the primary_version is populated
        # when the service is terminated. This should be fixed in the backend.
        is_terminated = model.current_state == ServiceEventCurrentState.TERMINATED

        # TODO(edoakes): this is currently only exposed at the service level in the API,
        # which means that the per-version `query_auth_token_enabled` field will lie if
        # it's changed.
        query_auth_token_enabled = model.auth_token is not None

        primary_version = None
        if not is_terminated and model.primary_version is not None:
            primary_version = self._service_version_model_to_status(
                model.primary_version,
                service_name=model.name,
                query_auth_token_enabled=query_auth_token_enabled,
            )

        canary_version = None
        if not is_terminated and model.canary_version is not None:
            canary_version = self._service_version_model_to_status(
                model.canary_version,
                service_name=model.name,
                query_auth_token_enabled=query_auth_token_enabled,
            )

        # If we add a new state to the backend, old clients may not recognize it.
        # Rather than erroring out and causing old code to crash, return UNKNOWN.
        try:
            state = ServiceState(model.current_state)
        except ValueError:
            state = ServiceState.UNKNOWN
            logger.warning(
                f"Got unrecognized state: '{model.current_state}'. "
                "You likely need to update the 'anyscale' package. "
                "If you still see this message after upgrading, contact Anyscale support."
            )

        return ServiceStatus(
            service_id=model.id,
            name=model.name,
            state=state,
            query_url=model.base_url,
            query_auth_token=model.auth_token,
            primary_version=primary_version,
            canary_version=canary_version,
        )

    def status(self, name: Optional[str] = None) -> ServiceStatus:
        if name is None:
            name = self._get_default_name()

        model: Optional[ServiceModel] = self._client.get_service(name)
        if model is None:
            raise RuntimeError(f"Service with name '{name}' was not found.")

        return self._service_model_to_status(model)
