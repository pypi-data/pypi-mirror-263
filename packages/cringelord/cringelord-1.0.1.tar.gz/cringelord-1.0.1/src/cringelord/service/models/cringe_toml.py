from pathlib import Path
from typing import Optional

from pydantic import BaseModel, DirectoryPath, FilePath
from pydantic import field_validator, model_validator

from .cringe_environment import CringeEnvironment
from .cringe_mode import CringeMode


class CringeTOML(BaseModel):
    config_file: FilePath
    mode: CringeMode = CringeMode.ALL
    environments: dict[str, list[CringeEnvironment]]

    src_dir: Optional[DirectoryPath] = Path.cwd()
    default_environment: Optional[str] = None
    templates: Optional[list[Path]] = None
    exception_on_missing_setting: Optional[bool] = True

    @classmethod
    @field_validator("config_file")
    def is_yaml_file(cls, config_file: FilePath):
        if config_file.suffix not in [".yaml", ".yml"]:
            raise ValueError("config_file must point to a YAML file.")

        return config_file

    @model_validator(mode="after")
    def ensure_default_environment_is_not_empty(self):
        if not self.default_environment:
            first_environment_name = next(iter(self.environments.keys()))
            self.default_environment = first_environment_name

        return self

    @model_validator(mode="after")
    def default_environment_should_exist(self):
        if not self.default_environment:
            return self

        if self.default_environment not in self.environments.keys():
            raise ValueError("Default environment does not exist.")

        return self

    def get_environment(self, environment_name):
        try:
            return self.environments[environment_name][0]
        except KeyError:
            return self.get_environment_from_aliases(environment_name)
        except IndexError:
            raise ValueError(f"Environment '{environment_name} is incorrect.")

    def get_environment_from_aliases(self, environment_name):
        for [environment] in self.environments.values():
            if environment_name in environment.aliases:
                return environment

    def get_all_environment_names(self):
        names = list(self.environments.keys())
        aliases = self.get_aliases()

        return names + aliases

    def get_aliases(self):
        aliases = []
        for [environment] in self.environments.values():
            aliases.extend(environment.aliases)

        return aliases
