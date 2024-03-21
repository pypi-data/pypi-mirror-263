from .env_names import EnvNames
from .exceptions import MissingSettingError, SettingMismatchError


class CringeConfig:
    def __init__(self, env_names: EnvNames, config_dict):
        self.current_env_name = env_names.current_env
        self.other_env_names = env_names.other_envs

        self.settings = self._construct_settings(config_dict)

    def get_settings(self):
        return self.settings

    def get_setting(self, name):
        try:
            return self.settings[name]
        except KeyError:
            raise MissingSettingError(name)

    def _construct_settings(self, config_dict):
        self._validate(config_dict)

        self._flatten_current_env_settings(config_dict)
        self._remove_other_env_settings(config_dict)

        return config_dict

    def _validate(self, config_dict):
        current_env_settings = config_dict[self.current_env_name]

        for key in config_dict:
            if key in self.other_env_names:
                self._validate_env(
                    config_dict=config_dict,
                    env_name=key,
                    current_env_settings=current_env_settings
                )

    def _validate_env(self, config_dict, env_name, current_env_settings):
        other_env_settings = config_dict[env_name]

        if set(current_env_settings) != set(other_env_settings):
            raise SettingMismatchError(
                env1_name=self.current_env_name,
                env2_name=env_name
            )

    def _flatten_current_env_settings(self, config_dict):
        config_dict |= config_dict.pop(self.current_env_name)

    def _remove_other_env_settings(self, config_dict):
        for env_name in self.other_env_names:
            if env_name in config_dict:
                del config_dict[env_name]
