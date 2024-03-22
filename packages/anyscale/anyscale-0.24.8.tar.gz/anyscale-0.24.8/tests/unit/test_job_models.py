from dataclasses import dataclass
import os
import re
from typing import Any, Dict, List, Optional, Union

import pytest

from anyscale.job.models import JobConfig


@dataclass
class JobConfigFile:
    name: str
    expected_config: Optional[JobConfig] = None
    expected_error: Optional[str] = None

    def get_path(self) -> str:
        return os.path.join(
            os.path.dirname(__file__), "test_files/job_config_files", self.name
        )


TEST_CONFIG_FILES = [
    JobConfigFile(
        "minimal.yaml", expected_config=JobConfig(entrypoint="python test.py"),
    ),
    JobConfigFile(
        "full.yaml",
        expected_config=JobConfig(
            name="test-name-from-file",
            image_uri="docker.io/library/test:latest",
            compute_config="test-compute-config",
            working_dir="test-working-dir",
            excludes=["test"],
            requirements=["pip-install-test"],
            entrypoint="python test.py",
            max_retries=5,
            runtime_env={"env_vars": {"HELLO": "WORLD"},},
        ),
    ),
    JobConfigFile(
        "points_to_requirements_file.yaml",
        expected_config=JobConfig(
            entrypoint="python test.py", requirements="some_requirements_file.txt",
        ),
    ),
    JobConfigFile(
        "unrecognized_option.yaml",
        expected_error=re.escape(
            "__init__() got an unexpected keyword argument 'bad_option'"
        ),
    ),
]


class TestJobConfig:
    def test_invalid_entrypoint(self):
        with pytest.raises(ValueError, match="'entrypoint' cannot be empty."):
            JobConfig()

        with pytest.raises(ValueError, match="'entrypoint' cannot be empty."):
            JobConfig(entrypoint="")

        with pytest.raises(TypeError, match="'entrypoint' must be a string."):
            JobConfig(entrypoint=b"oops")

    def test_invalid_max_retries(self):
        with pytest.raises(TypeError, match="'max_retries' must be an int."):
            JobConfig(entrypoint="python test.py", max_retries="1")

        with pytest.raises(ValueError, match="'max_retries' must be >= 0."):
            JobConfig(entrypoint="python test.py", max_retries=-1)

    def test_options(self):
        config = JobConfig(entrypoint="python test.py")

        options = {
            "name": "test-name",
            "image_uri": "docker.io/libaray/test-image:latest",
            "compute_config": "test-compute-config",
            "requirements": ["pip-install-test"],
            "working_dir": ".",
            "excludes": ["some-path"],
            "max_retries": 100,
        }

        # Test setting fields one at a time.
        for option, val in options.items():
            assert config.options(**{option: val}) == JobConfig(
                entrypoint="python test.py", **{option: val}
            )

        # Test setting fields all at once.
        assert config.options(**options) == JobConfig(
            entrypoint="python test.py", **options
        )

    @pytest.mark.skip(reason="This logic will be moved to the SDK.")
    @pytest.mark.parametrize(
        ("working_dir", "excludes"),
        [
            (None, None),
            (".", ["path1/", "path2"]),
            ("s3://path.zip", ["path1/", "path2"]),
        ],
    )
    def test_override_working_dir_excludes(
        self, working_dir: Optional[str], excludes: Optional[List[str]]
    ):
        starting_runtime_envs: List[Optional[Dict[str, Any]]] = [
            None,
            {},
            {
                "excludes": ["something-else"],
                "working_dir": "s3://somewhere.zip",
                "env_vars": {"abc": "123"},
            },
        ]

        jobs = [
            JobConfig(
                entrypoint="python test.py",
                working_dir=working_dir,
                excludes=excludes,
                runtime_env=runtime_env,
            )
            for runtime_env in starting_runtime_envs
        ]

        if working_dir is None:
            assert excludes is None
            assert [job.runtime_env for job in jobs] == starting_runtime_envs
        else:
            assert isinstance(excludes, list)
            assert len(jobs) == 3
            assert jobs[0].runtime_env == {
                "working_dir": working_dir,
                "excludes": excludes,
            }
            assert jobs[1].runtime_env == {
                "working_dir": working_dir,
                "excludes": excludes,
            }
            assert jobs[2].runtime_env == {
                "working_dir": working_dir,
                # Existing `excludes` field should be extended.
                "excludes": ["something-else", *excludes],
                "env_vars": {"abc": "123"},
            }

    @pytest.mark.skip(reason="This logic will be moved to the SDK.")
    @pytest.mark.parametrize(
        ("requirements"), [(None), ("./requirements.txt"), (["req1", "req2"]),],
    )
    def test_override_requirements(
        self, requirements: Union[None, str, List[str]],
    ):
        starting_runtime_envs: List[Optional[Dict[str, Any]]] = [
            None,
            {},
            {"pip": ["something", "else"], "env_vars": {"abc": "123"},},
        ]

        jobs = [
            JobConfig(
                entrypoint="python test.py",
                requirements=requirements,
                runtime_env=runtime_env,
            )
            for runtime_env in starting_runtime_envs
        ]

        if requirements is None:
            assert [job.runtime_env for job in jobs] == starting_runtime_envs
        else:
            assert len(jobs) == 3
            assert jobs[0].runtime_env == {
                "pip": requirements,
            }
            assert jobs[0].runtime_env == {
                "pip": requirements,
            }
            assert jobs[2].runtime_env == {
                "pip": requirements,
                "env_vars": {"abc": "123"},
            }

    @pytest.mark.parametrize("config_file", TEST_CONFIG_FILES)
    def test_from_config_file(self, config_file: JobConfigFile):
        if config_file.expected_error is not None:
            with pytest.raises(Exception, match=config_file.expected_error):
                JobConfig.from_yaml(config_file.get_path())

            return

        assert config_file.expected_config == JobConfig.from_yaml(
            config_file.get_path()
        )
