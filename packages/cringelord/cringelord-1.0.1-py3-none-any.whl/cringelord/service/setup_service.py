import json
import os
import warnings
import yaml

from .models import CringeConfig, CringeTOML, EnvNames


class SetupService:
    def __init__(self, cringe_toml: CringeTOML, env_name: str = None):
        """
        Sets up the Cringelord tool.

        Args:
            cringe_toml (CringeTOML): The configuration for Cringelord itself.
            env_name: The name of the environment for which to set up
                Cringelord.
        """
        self.cringe_toml = cringe_toml
        self.current_env = env_name or cringe_toml.default_environment

    def setup(self):
        for name, value in self._get_settings():
            print(f"Setting {name} to {value}.")
            os.environ[name] = json.dumps(value)

    def _determine_current_env(self, env_name):
        if not env_name:
            warnings.warn("$ENVIRONMENT_NAME not set. Using default.")
            return self.cringe_toml.default_environment

        return env_name

    def _get_settings(self):
        cringe_config = self._create_cringe_config()

        return cringe_config.get_settings().items()

    def _create_cringe_config(self):
        contents = self.cringe_toml.config_file.read_text()
        env_names = EnvNames(
            current_env=self.current_env,
            other_envs=self.cringe_toml.get_all_environment_names()
        )

        return CringeConfig(
            env_names=env_names,
            config_dict=yaml.safe_load(contents)
        )
