import os
from pathlib import Path

from .exceptions import SetupError
from .toml_parser import get_toml_parser
from cringelord.service import SetupService
from cringelord.service.models import CringeTOML


def setup_cringelord():
    cringe_toml_dict = _get_cringe_toml_dict()
    cringe_toml = CringeTOML(**cringe_toml_dict)

    setup_service = SetupService(
        cringe_toml=cringe_toml,
        env_name=os.getenv("ENVIRONMENT_NAME")
    )

    setup_service.setup()

    return cringe_toml


def _get_cringe_toml_dict():
    pyproject_path = Path.cwd() / "pyproject.toml"
    pyproject = _parse_pyproject(pyproject_path.read_text())

    return _get_cringelord_part(pyproject)


def _get_cringelord_part(pyproject):
    try:
        return pyproject["tool"]["cringelord"]
    except KeyError:
        raise SetupError("Your pyproject.toml is not set up for Cringelord.")


def _parse_pyproject(pyproject_contents):
    parser = get_toml_parser()

    return parser.loads(pyproject_contents)
