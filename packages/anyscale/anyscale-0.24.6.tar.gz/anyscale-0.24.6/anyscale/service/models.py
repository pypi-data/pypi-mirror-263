import copy
from dataclasses import dataclass, field
from enum import Enum
import re
from typing import Any, Dict, List, Optional, Union

from anyscale._private.models import ModelBase


IMAGE_URI_PATTERN = re.compile(
    r"^"
    # Optional registry host: hostname with optional port
    r"((?P<host>[a-zA-Z0-9.-]+)(?::(?P<port>[0-9]+))?/)?"
    # Repository name: user_name/repository
    r"(?P<repository>[a-zA-Z0-9-_]+/([a-zA-Z0-9-/_])+)"
    # Optional Tag: version or string after ':'
    r"(:(?P<tag>[a-zA-Z0-9_.-]+))?"
    # Optional Digest: string after '@'
    # Note that when both tag and digest are provided, the tag is ignored.
    r"(@(?P<digest>[a-zA-Z0-9]+))?"
    r"$"
)


@dataclass(frozen=True)
class ServiceConfig(ModelBase):
    applications: List[Dict[str, Any]] = field(repr=False)
    name: Optional[str] = field(default=None)
    image_uri: Optional[str] = field(default=None)
    containerfile: Optional[str] = field(default=None, repr=False)
    compute_config: Optional[Union[Dict, str]] = field(default=None)
    working_dir: Optional[str] = field(default=None, repr=False)
    excludes: Optional[List[str]] = field(default=None, repr=False)
    requirements: Optional[Union[str, List[str]]] = field(default=None, repr=False)
    query_auth_token_enabled: bool = field(default=True, repr=False)
    grpc_options: Optional[Dict[str, Any]] = field(default=None, repr=False)
    http_options: Optional[Dict[str, Any]] = field(default=None, repr=False)
    ray_gcs_external_storage_config: Optional[Dict[str, Any]] = field(
        default=None, repr=False
    )

    def __post_init__(self):
        super().__post_init__()
        self._override_application_runtime_envs()

    def _override_application_runtime_envs(self):
        """Override the runtime_env field of the provided applications.

        Fields that are modified:
            - 'working_dir' is overwritten with the passed working_dir.
            - 'pip' is overwritten with the passed requirements.
            - 'excludes' is extended with the passed excludes list.
        """
        applications = copy.deepcopy(self.applications)
        for application in applications:
            runtime_env = application.get("runtime_env", {})
            if self.working_dir is not None:
                runtime_env["working_dir"] = self.working_dir

            if self.excludes is not None:
                # Extend the list of excludes rather than overwriting it.
                runtime_env["excludes"] = (
                    runtime_env.get("excludes", []) + self.excludes
                )

            if self.requirements is not None:
                runtime_env["pip"] = self.requirements

            if runtime_env:
                application["runtime_env"] = runtime_env

        # Need to use `object.__setattr__` because `frozen=True` on the dataclass.
        object.__setattr__(self, "applications", applications)
        # Clear `excludes`, `working_dir`, `requirements` in order to avoid re-applying
        # them every time `.options()` is called.
        object.__setattr__(self, "excludes", None)
        object.__setattr__(self, "working_dir", None)
        object.__setattr__(self, "requirements", None)

    def _validate_applications(self, applications: List[Dict[str, Any]]):
        if not isinstance(applications, list):
            raise TypeError("'applications' must be a list.")
        if len(applications) == 0:
            raise ValueError("'applications' cannot be empty.")

        # Validate import paths.
        for app in applications:
            import_path = app.get("import_path", None)
            if not import_path:
                raise ValueError("Every application must specify an import path.")

            if not isinstance(import_path, str):
                raise TypeError(f"'import_path' must be a string, got: {import_path}")

            if (
                import_path.count(":") != 1
                or import_path.rfind(":") in {0, len(import_path) - 1}
                or import_path.rfind(".") in {0, len(import_path) - 1}
            ):
                raise ValueError(
                    f"'import_path' must be of the form: 'module.optional_submodule:app', but got: '{import_path}'."
                )

    def _validate_name(self, name: Optional[str]):
        if name is not None and not isinstance(name, str):
            raise TypeError("'name' must be a string.")

    def _validate_image_uri(self, image_uri: Optional[str]):
        if image_uri is None:
            return

        if not isinstance(image_uri, str):
            raise TypeError("'image_uri' must be a string.")

        matches = IMAGE_URI_PATTERN.match(image_uri)
        if not matches:
            raise ValueError(
                f"Invalid image URI: '{image_uri}'. Must be in the format: [registry_host/]user_name/repository[:tag][@digest]."
            )

    def _validate_containerfile(self, containerfile: Optional[str]):
        if containerfile is not None and not isinstance(containerfile, str):
            raise TypeError("'containerfile' must be a string.")

    def _validate_compute_config(self, compute_config: Optional[Union[Dict, str]]):
        if compute_config is not None and not isinstance(compute_config, (str, dict)):
            raise TypeError("'compute_config' must be a string or dictionary.")

    def _validate_working_dir(self, working_dir: Optional[str]):
        if working_dir is not None and not isinstance(working_dir, str):
            raise TypeError("'working_dir' must be a string.")

    def _validate_requirements(self, requirements: Optional[Union[str, List[str]]]):
        if requirements is None or isinstance(requirements, str):
            return

        if not isinstance(requirements, list) or not all(
            isinstance(r, str) for r in requirements
        ):
            raise TypeError(
                "'requirements' must be a strings (file path) or list of strings."
            )

    def _validate_excludes(self, excludes: Optional[List[str]]):
        if excludes is not None and (
            not isinstance(excludes, list)
            or not all(isinstance(e, str) for e in excludes)
        ):
            raise TypeError("'excludes' must be a list of strings.")

    def _validate_query_auth_token_enabled(self, query_auth_token_enabled: bool):
        if not isinstance(query_auth_token_enabled, bool):
            raise TypeError("'query_auth_token_enabled' must be a boolean.")

    def _validate_grpc_options(self, grpc_options: Optional[Dict[str, Any]]):
        """Validate the `grpc_options` field.

        This will be passed through as part of the Ray Serve config, but some fields are
        disallowed (not valid when deploying Anyscale services).
        """
        if grpc_options is None:
            return
        elif not isinstance(grpc_options, dict):
            raise TypeError("'grpc_options' must be a dict.")

        banned_options = {
            "port",
        }
        banned_options_passed = {o for o in banned_options if o in grpc_options}
        if len(banned_options_passed) > 0:
            raise ValueError(
                "The following provided 'grpc_options' are not permitted "
                f"in Anyscale: {banned_options_passed}."
            )

    def _validate_http_options(self, http_options: Optional[Dict[str, Any]]):
        """Validate the `http_options` field.

        This will be passed through as part of the Ray Serve config, but some fields are
        disallowed (not valid when deploying Anyscale services).
        """
        if http_options is None:
            return
        elif not isinstance(http_options, dict):
            raise TypeError("'http_options' must be a dict.")

        banned_options = {"host", "port", "root_path"}
        banned_options_passed = {o for o in banned_options if o in http_options}
        if len(banned_options_passed) > 0:
            raise ValueError(
                "The following provided 'http_options' are not permitted "
                f"in Anyscale: {banned_options_passed}."
            )

    def _validate_ray_gcs_external_storage_config(
        self, ray_gcs_external_storage_config: Optional[Dict[str, Any]]
    ):
        if ray_gcs_external_storage_config is not None and not isinstance(
            ray_gcs_external_storage_config, dict
        ):
            raise TypeError("'ray_gcs_external_storage_config' must be a dict.")


class ServiceState(str, Enum):
    UNKNOWN = "UNKNOWN"
    STARTING = "STARTING"
    RUNNING = "RUNNING"
    # TODO(edoakes): UPDATING comes up while rolling out and rolling back.
    # This is very unexpected from a customer's point of view, we should fix it.
    UPDATING = "UPDATING"
    ROLLING_OUT = "ROLLING_OUT"
    ROLLING_BACK = "ROLLING_BACK"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    UNHEALTHY = "UNHEALTHY"
    SYSTEM_FAILURE = "SYSTEM_FAILURE"

    def __str__(self):
        return self.name


# TODO(edoakes): we should have a corresponding ServiceVersionState.
@dataclass(frozen=True)
class ServiceVersionStatus(ModelBase):
    name: str
    weight: int
    config: ServiceConfig = field(repr=False)

    def _validate_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'name' must be a string.")

    def _validate_weight(self, weight: int):
        if not isinstance(weight, int):
            raise TypeError("'weight' must be an int.")

    def _validate_config(self, config: ServiceConfig):
        if not isinstance(config, ServiceConfig):
            raise TypeError("'config' must be a ServiceConfig.")


@dataclass(frozen=True)
class ServiceStatus(ModelBase):
    name: str
    service_id: str
    state: ServiceState
    query_url: str = field(repr=False)
    query_auth_token: Optional[str] = field(default=None, repr=False)
    primary_version: Optional[ServiceVersionStatus] = field(default=None, repr=False)
    canary_version: Optional[ServiceVersionStatus] = field(default=None, repr=False)

    def _validate_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("'name' must be a string.")

    def _validate_service_id(self, service_id: str):
        if not isinstance(service_id, str):
            raise TypeError("'service_id' must be a string.")

    def _validate_state(self, state: ServiceState):
        if isinstance(state, str):
            # This will raise a ValueError if the state is unrecognized.
            object.__setattr__(self, "state", ServiceState(state))
        elif not isinstance(state, ServiceState):
            raise TypeError("'state' must be a ServiceState.")

    def _validate_query_url(self, query_url: str):
        if not isinstance(query_url, str):
            raise TypeError("'query_url' must be a string.")

    def _validate_query_auth_token(self, query_auth_token: Optional[str]):
        if query_auth_token is not None and not isinstance(query_auth_token, str):
            raise TypeError("'query_auth_token' must be a string.")

    def _validate_primary_version(
        self, primary_version: Optional[ServiceVersionStatus]
    ):
        if primary_version is not None and not isinstance(
            primary_version, ServiceVersionStatus
        ):
            raise TypeError("'primary_version' must be a ServiceVersionStatus.")

    def _validate_canary_version(self, canary_version: Optional[ServiceVersionStatus]):
        if canary_version is not None and not isinstance(
            canary_version, ServiceVersionStatus
        ):
            raise TypeError("'canary_version' must be a ServiceVersionStatus.")
