from dataclasses import dataclass, field
import re
from typing import Dict, List, Optional, Union

from anyscale._private.models import ModelBase


IMAGE_URI_PATTERN = "[registry_host/]user_name/repository[:tag][@digest]"
IMAGE_URI_PATTERN_RE = re.compile(
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
class WorkloadConfig(ModelBase):
    name: Optional[str] = field(default=None)

    def _validate_name(self, name: Optional[str]):
        if name is not None and not isinstance(name, str):
            raise TypeError("'name' must be a string.")

    image_uri: Optional[str] = field(default=None)

    def _validate_image_uri(self, image_uri: Optional[str]):
        if image_uri is None:
            return

        if not isinstance(image_uri, str):
            raise TypeError("'image_uri' must be a string.")

        matches = IMAGE_URI_PATTERN_RE.match(image_uri)
        if not matches:
            raise ValueError(
                f"Invalid image URI: '{image_uri}'. Must be in the format: '{IMAGE_URI_PATTERN}'."
            )

    containerfile: Optional[str] = field(default=None, repr=False)

    def _validate_containerfile(self, containerfile: Optional[str]):
        if containerfile is not None and not isinstance(containerfile, str):
            raise TypeError("'containerfile' must be a string.")

    compute_config: Optional[Union[Dict, str]] = field(default=None)

    def _validate_compute_config(self, compute_config: Optional[Union[Dict, str]]):
        if compute_config is not None and not isinstance(compute_config, (str, dict)):
            raise TypeError("'compute_config' must be a string or dictionary.")

    working_dir: Optional[str] = field(default=None, repr=False)

    def _validate_working_dir(self, working_dir: Optional[str]):
        if working_dir is not None and not isinstance(working_dir, str):
            raise TypeError("'working_dir' must be a string.")

    excludes: Optional[List[str]] = field(default=None, repr=False)

    def _validate_excludes(self, excludes: Optional[List[str]]):
        if excludes is not None and (
            not isinstance(excludes, list)
            or not all(isinstance(e, str) for e in excludes)
        ):
            raise TypeError("'excludes' must be a list of strings.")

    requirements: Optional[Union[str, List[str]]] = field(default=None, repr=False)

    def _validate_requirements(self, requirements: Optional[Union[str, List[str]]]):
        if requirements is None or isinstance(requirements, str):
            return

        if not isinstance(requirements, list) or not all(
            isinstance(r, str) for r in requirements
        ):
            raise TypeError(
                "'requirements' must be a string (file path) or list of strings."
            )
