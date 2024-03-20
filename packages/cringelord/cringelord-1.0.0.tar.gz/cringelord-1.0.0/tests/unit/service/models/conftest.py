import os
from pathlib import Path

import pytest

from cringelord.service.models.cringe_environment import CringeEnvironment


@pytest.fixture(scope="package")
def env_description():
    return "Our cool test environment"


@pytest.fixture(scope="package")
def env_aliases():
    return [
        "dev",
        "development",
        "test",
        "tst"
    ]


@pytest.fixture(scope="package")
def cringe_env(env_description, env_aliases):
    return CringeEnvironment(
        description=env_description,
        aliases=env_aliases
    )


@pytest.fixture
def abs_config_path(tmp_path):
    path = tmp_path / "cringe-config.yaml"
    path.write_text("Empty file for testing")

    yield path

    path.unlink()


@pytest.fixture
def rel_config_path(tmp_path):
    original_cwd = Path.cwd()
    new_cwd = tmp_path
    rel_path = "some_dir/cringe-config.yaml"

    abs_path = tmp_path / rel_path
    abs_path.parent.mkdir(parents=True, exist_ok=True)
    abs_path.write_text("Empty file for testing")

    os.chdir(new_cwd)

    yield rel_path

    os.chdir(original_cwd)

