import logging
import pathlib
import re
import time
from typing import Callable, Dict, List, Optional, Tuple

import requests

from anyscale._private.anyscale_client.common import (
    AnyscaleClientInterface,
    DEFAULT_PYTHON_VERSION,
    DEFAULT_RAY_VERSION,
    RUNTIME_ENV_PACKAGE_FORMAT,
)
from anyscale.authenticate import AuthenticationBlock, get_auth_api_client
from anyscale.cli_logger import BlockLogger
from anyscale.client.openapi_client.api.default_api import DefaultApi as InternalApi
from anyscale.client.openapi_client.models import (
    ArchiveStatus,
    CloudDataBucketFileType,
    CloudDataBucketPresignedUploadInfo,
    CloudDataBucketPresignedUploadRequest,
    ComputeTemplateConfig,
    ComputeTemplateQuery,
    CreateComputeTemplate,
    DecoratedComputeTemplate,
)
from anyscale.cluster_compute import parse_cluster_compute_name_version
from anyscale.sdk.anyscale_client.api.default_api import DefaultApi as ExternalApi
from anyscale.sdk.anyscale_client.models import (
    ApplyServiceModel,
    Cloud,
    Cluster,
    ClusterCompute,
    ClusterComputeConfig,
    ClusterEnvironment,
    ClusterEnvironmentBuild,
    ClusterEnvironmentBuildStatus,
    Project,
    RollbackServiceModel,
    ServiceModel,
)
from anyscale.sdk.anyscale_client.models.create_cluster_environment import (
    CreateClusterEnvironment,
)
from anyscale.sdk.anyscale_client.models.create_cluster_environment_build import (
    CreateClusterEnvironmentBuild,
)
from anyscale.sdk.anyscale_client.rest import ApiException
from anyscale.util import (
    get_cluster_model_for_current_workspace,
    get_endpoint,
    is_anyscale_workspace,
)
from anyscale.utils.runtime_env import (
    is_workspace_dependency_tracking_disabled,
    WORKSPACE_REQUIREMENTS_FILE_PATH,
    zip_local_dir,
)
from anyscale.utils.workspace_notification import (
    WORKSPACE_NOTIFICATION_ADDRESS,
    WorkspaceNotification,
)


block_logger = BlockLogger()
logger = logging.getLogger(__name__)


class AnyscaleClient(AnyscaleClientInterface):
    # Number of entries to fetch per request for list endpoints.
    LIST_ENDPOINT_COUNT = 50

    def __init__(
        self,
        *,
        api_clients: Optional[Tuple[ExternalApi, InternalApi]] = None,
        sleep: Optional[Callable[[float], None]] = None,
        workspace_requirements_file_path: str = WORKSPACE_REQUIREMENTS_FILE_PATH,
    ):
        if api_clients is None:
            auth_block: AuthenticationBlock = get_auth_api_client(
                raise_structured_exception=True
            )
            api_clients = (auth_block.anyscale_api_client, auth_block.api_client)

        self._external_api_client, self._internal_api_client = api_clients
        self._workspace_requirements_file_path = workspace_requirements_file_path
        self._sleep = sleep or time.sleep

        # Cached IDs and models to avoid duplicate lookups.
        self._default_project_id: Optional[str] = None
        self._cloud_id_cache: Dict[Optional[str], str] = {}
        self._current_workspace_cluster: Optional[Cluster] = None

    def get_service_ui_url(self, service_id: str) -> str:
        return get_endpoint(f"/services/{service_id}")

    def inside_workspace(self) -> bool:
        return self.get_current_workspace_cluster() is not None

    def get_workspace_requirements_path(self) -> Optional[str]:
        if (
            not self.inside_workspace()
            or is_workspace_dependency_tracking_disabled()
            or not pathlib.Path(self._workspace_requirements_file_path).is_file()
        ):
            return None

        return self._workspace_requirements_file_path

    def get_current_workspace_cluster(self) -> Optional[Cluster]:
        # Checks for the existence of the ANYSCALE_EXPERIMENTAL_WORKSPACE_ID env var.
        if not is_anyscale_workspace():
            return None

        if self._current_workspace_cluster is None:
            # Picks up the cluster ID from the ANYSCALE_SESSION_ID env var.
            self._current_workspace_cluster = get_cluster_model_for_current_workspace(
                self._external_api_client
            )

        return self._current_workspace_cluster

    def get_project_id(self) -> str:
        workspace_cluster = self.get_current_workspace_cluster()
        if workspace_cluster is not None:
            return workspace_cluster.project_id

        if self._default_project_id is None:
            default_project: Project = self._external_api_client.get_default_project().result
            self._default_project_id = default_project.id

        return self._default_project_id

    def _get_cloud_id_for_compute_config_id(self, compute_config_id: str) -> str:
        cluster_compute: ClusterCompute = self._external_api_client.get_cluster_compute(
            compute_config_id
        ).result
        cluster_compute_config: ClusterComputeConfig = cluster_compute.config
        return cluster_compute_config.cloud_id

    def get_cloud_id(
        self, cloud_name: Optional[str] = None, compute_config_id: Optional[str] = None
    ) -> Optional[str]:
        if cloud_name is not None:
            raise NotImplementedError("Only default cloud is currently implemented.")

        if compute_config_id is not None:
            return self._get_cloud_id_for_compute_config_id(compute_config_id)

        if cloud_name in self._cloud_id_cache:
            return self._cloud_id_cache[cloud_name]

        workspace_cluster = self.get_current_workspace_cluster()
        if workspace_cluster is not None:
            # NOTE(edoakes): the Cluster model has a compute_config_config model that includes
            # its cloud ID, but it's not always populated.
            # TODO(edoakes): add cloud_id to the Cluster model to avoid a second RTT.
            cloud_id = self._get_cloud_id_for_compute_config_id(
                workspace_cluster.cluster_compute_id
            )
        else:
            result: Cloud = self._external_api_client.get_default_cloud().result
            cloud_id = result.id

        self._cloud_id_cache[cloud_name] = cloud_id
        return cloud_id

    def create_anonymous_compute_config(self, config: ComputeTemplateConfig) -> str:
        return self._internal_api_client.create_compute_template_api_v2_compute_templates_post(
            create_compute_template=CreateComputeTemplate(
                config=config, anonymous=True,
            )
        ).result.id

    def get_compute_config(
        self, compute_config_id: str
    ) -> Optional[DecoratedComputeTemplate]:
        try:
            cluster_compute: ClusterCompute = self._internal_api_client.get_compute_template_api_v2_compute_templates_template_id_get(
                compute_config_id
            ).result
            return cluster_compute
        except ApiException as e:
            if e.status == 404:
                return None

            raise e from None

    def get_compute_config_id(
        self, compute_config_name: Optional[str] = None
    ) -> Optional[str]:
        if compute_config_name is not None:
            name, version = parse_cluster_compute_name_version(compute_config_name)
            if version is None:
                # Setting `version=-1` will return only the latest version if there are multiple.
                version = -1
            cluster_computes = self._internal_api_client.search_compute_templates_api_v2_compute_templates_search_post(
                ComputeTemplateQuery(
                    orgwide=True,
                    name={"equals": name},
                    include_anonymous=True,
                    archive_status=ArchiveStatus.NOT_ARCHIVED,
                    version=version,
                )
            ).results

            if len(cluster_computes) == 0:
                return None

            compute_template: DecoratedComputeTemplate = cluster_computes[0]
            return compute_template.id

        # If the compute config name is not provided, we pick an appropriate default.
        #
        #   - If running in a workspace, we use the workspace's compute config, with
        #     a minor transformation if auto_select_worker_config is applied.
        #
        #   - Otherwise, we use the default compute config provided by the API.

        workspace_cluster = self.get_current_workspace_cluster()
        if workspace_cluster is not None:
            workspace_compute_config: DecoratedComputeTemplate = self.get_compute_config(
                workspace_cluster.cluster_compute_id
            )
            workspace_config: ClusterComputeConfig = workspace_compute_config.config
            if workspace_config.auto_select_worker_config:
                workspace_config = self._apply_standardized_head_node_type(
                    workspace_config
                )
                return self.create_anonymous_compute_config(workspace_config)
            else:
                return workspace_cluster.cluster_compute_id

        # NOTE(edoakes): for some reason the API endpoint is called "cluster compute" but this
        # is the non-deprecated API to use for compute configs.
        return self._external_api_client.get_default_cluster_compute().result.id

    def _apply_standardized_head_node_type(
        self, compute_config: ClusterComputeConfig
    ) -> ClusterComputeConfig:
        """
        Apply the following transformations to the provided compute config:

        1. Standardize the head node instance type.
        2. Disable scheduling on the head node.
        """
        # Retrieve the default cluster compute config.
        default_compute_config: DecoratedComputeTemplate = self._external_api_client.get_default_cluster_compute().result.config

        # Standardize the head node instance type.
        compute_config.head_node_type.instance_type = (
            default_compute_config.head_node_type.instance_type
        )

        # Disable scheduling on the head node.
        if compute_config.head_node_type.resources is None:
            compute_config.head_node_type.resources = {}
        compute_config.head_node_type.resources["CPU"] = 0

        return compute_config

    def get_cluster_env_build_image_uri(
        self, cluster_env_build_id: str
    ) -> Optional[str]:
        try:
            build: ClusterEnvironmentBuild = self._external_api_client.get_cluster_environment_build(
                cluster_env_build_id
            ).result
            return build.docker_image_name
        except ApiException as e:
            if e.status == 404:
                return None

            raise e from None

    def get_default_build_id(self) -> str:
        """Get default build id.

        If running in a workspace, it will return the workspace's cluster environment build ID.
        Else it will return the default cluster environment build ID.
        """
        workspace_cluster = self.get_current_workspace_cluster()
        if workspace_cluster is not None:
            return workspace_cluster.cluster_environment_build_id
        result: ClusterEnvironmentBuild = self._external_api_client.get_default_cluster_environment_build(
            DEFAULT_PYTHON_VERSION, DEFAULT_RAY_VERSION,
        ).result
        return result.id

    @staticmethod
    def _get_cluster_env_name_from_image_uri(image_uri: str) -> str:
        if len(image_uri) == 0:
            raise ValueError("image_uri cannot be empty.")

        pattern = re.compile("^[A-Za-z0-9_-]+$")
        # Keep only characters that match the pattern
        escaped = []
        for c in image_uri:
            if not pattern.match(c):
                escaped.append("-")
            else:
                escaped.append(c)
        return "".join(escaped)

    def _get_cluster_env_by_name(self, name: str) -> Optional[ClusterEnvironment]:
        cluster_envs = self._external_api_client.search_cluster_environments(
            {
                "name": {"equals": name},
                "paging": {"count": 1},
                "include_anonymous": True,
            }
        ).results
        return cluster_envs[0] if cluster_envs else None

    def _wait_for_build_to_succeed(
        self, build_id: str, poll_interval_seconds=3, timeout_secs=3600,
    ):
        """Periodically check the status of the build operation until it completes.
        Raise a RuntimeError if the build fails or cancelled.
        Raise a TimeoutError if the build does not complete within the timeout.
        """
        elapsed_secs = 0
        block_logger.info(
            f"Waiting for cluster environment build ({build_id}) to complete."
        )
        while elapsed_secs < timeout_secs:
            build = self._external_api_client.get_cluster_environment_build(
                build_id
            ).result
            if build.status == ClusterEnvironmentBuildStatus.SUCCEEDED:
                return
            elif build.status == ClusterEnvironmentBuildStatus.FAILED:
                raise RuntimeError(f"Image build {build_id} failed.")
            elif build.status == ClusterEnvironmentBuildStatus.CANCELED:
                raise RuntimeError(f"Image build {build_id} unexpectedly cancelled.")

            elapsed_secs += poll_interval_seconds
            block_logger.info(
                f"Waiting for image build to complete. Elapsed time: {elapsed_secs} seconds",
            )
            self._sleep(poll_interval_seconds)
        raise TimeoutError(
            f"Timed out waiting for image build {build_id} to complete after {timeout_secs}s."
        )

    def _find_or_create_cluster_env(self, cluster_env_name: str) -> ClusterEnvironment:
        existing_cluster_env = self._get_cluster_env_by_name(cluster_env_name)
        if existing_cluster_env is not None:
            return existing_cluster_env

        # this creates a cluster env only and it does not trigger a build to avoid the race condition
        # when creating a cluster environment and a build at the same time and then list builds for the cluster environment later.
        # ```
        #     cluster_env == self._external_api_client.create_cluster_environment(..., image_uri=image_uri)
        #     build == self._external_api_client.create_cluster_environment_build(..., cluster_env_id=cluster_env.id)
        # ```
        # The race condition can happen if another build for the same cluster envrionment is created between the two calls.
        cluster_environment = self._external_api_client.create_cluster_environment(
            CreateClusterEnvironment(name=cluster_env_name, anonymous=True)
        ).result
        return cluster_environment

    def get_cluster_env_build_id_from_containerfile(
        self, cluster_env_name: str, containerfile: str
    ) -> str:
        cluster_env = self._find_or_create_cluster_env(cluster_env_name)
        cluster_env_builds = self._external_api_client.list_cluster_environment_builds(
            cluster_environment_id=cluster_env.id, count=self.LIST_ENDPOINT_COUNT
        ).results
        for build in cluster_env_builds:
            if (
                build.status == ClusterEnvironmentBuildStatus.SUCCEEDED
                and build.containerfile == containerfile
            ):
                return build.id

        build_op = self._external_api_client.create_cluster_environment_build(
            CreateClusterEnvironmentBuild(
                cluster_environment_id=cluster_env.id, containerfile=containerfile,
            )
        ).result

        self._wait_for_build_to_succeed(build_op.cluster_environment_build_id)

        return build_op.cluster_environment_build_id

    def get_cluster_env_build_id(self, image_uri: str) -> str:
        cluster_env_name = self._get_cluster_env_name_from_image_uri(image_uri)
        cluster_env = self._find_or_create_cluster_env(cluster_env_name)

        # since we encode the image_uri into the cluster env name, there should exist one and only one build that matches the image_uri.
        cluster_env_builds = self._external_api_client.list_cluster_environment_builds(
            cluster_environment_id=cluster_env.id, count=1
        ).results
        build = cluster_env_builds[0] if cluster_env_builds else None
        if (
            build is not None
            and build.docker_image_name == image_uri
            and build.status == ClusterEnvironmentBuildStatus.SUCCEEDED
        ):
            return build.id

        # Still create a new build if the cluster env already exists but the build does not match the image_uri.
        result = self._external_api_client.create_cluster_environment_build(
            CreateClusterEnvironmentBuild(
                # For historical reasons, we have to use docker_image_name instead of image_uri; but it is just a URI to the image.
                cluster_environment_id=cluster_env.id,
                docker_image_name=image_uri,
            )
        ).result

        assert result.completed
        return result.cluster_environment_build_id

    def send_workspace_notification(
        self, notification: WorkspaceNotification,
    ):
        if not self.inside_workspace():
            return

        try:
            r = requests.post(WORKSPACE_NOTIFICATION_ADDRESS, json=notification.dict())
            r.raise_for_status()
        except Exception:
            logger.exception(
                "Failed to send workspace notification. "
                "This should not happen, so please contact Anyscale support."
            )

    def get_service(self, name: str) -> Optional[ServiceModel]:
        # TODO(edoakes): this endpoint is very slow and there's no reason we should need
        # to use this complex list endpoint just to fetch a service by name.
        paging_token = None
        project_id = self.get_project_id()
        service: Optional[ServiceModel] = None
        while True:
            resp = self._external_api_client.list_services(
                project_id=project_id,
                name=name,
                count=self.LIST_ENDPOINT_COUNT,
                paging_token=paging_token,
            )
            for result in resp.results:
                if result.name == name:
                    service = result
                    break

            paging_token = resp.metadata.next_paging_token
            if service is not None or paging_token is None:
                break

        return service

    def rollout_service(self, model: ApplyServiceModel) -> ServiceModel:
        result: ServiceModel = self._external_api_client.rollout_service(model).result
        return result

    def rollback_service(
        self, service_id: str, *, max_surge_percent: Optional[int] = None
    ) -> ServiceModel:
        result: ServiceModel = self._external_api_client.rollback_service(
            service_id,
            rollback_service_model=RollbackServiceModel(
                max_surge_percent=max_surge_percent
            ),
        )
        return result

    def terminate_service(self, service_id: str) -> ServiceModel:
        result: ServiceModel = self._external_api_client.terminate_service(service_id)
        return result

    def upload_local_dir_to_cloud_storage(
        self, local_dir: str, *, cloud_id: str, excludes: Optional[List[str]] = None
    ) -> str:
        if not pathlib.Path(local_dir).is_dir():
            raise RuntimeError(f"Path '{local_dir}' is not a valid directory.")

        with zip_local_dir(local_dir, excludes=excludes) as (
            _,
            zip_file_bytes,
            content_hash,
        ):
            request = CloudDataBucketPresignedUploadRequest(
                file_type=CloudDataBucketFileType.RUNTIME_ENV_PACKAGES,
                file_name=RUNTIME_ENV_PACKAGE_FORMAT.format(content_hash=content_hash),
            )
            info: CloudDataBucketPresignedUploadInfo = self._internal_api_client.generate_cloud_data_bucket_presigned_upload_url_api_v2_clouds_cloud_id_generate_cloud_data_bucket_presigned_upload_url_post(
                cloud_id, request
            ).result
            requests.put(info.upload_url, data=zip_file_bytes).raise_for_status()

        return info.file_uri
