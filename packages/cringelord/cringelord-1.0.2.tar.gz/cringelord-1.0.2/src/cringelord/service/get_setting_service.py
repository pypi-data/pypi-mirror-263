import json
import os

from .exceptions import MissingSettingError


class GetSettingService:
    def __init__(self, cringe_toml):
        self.cringe_toml = cringe_toml

    def get_setting(self, name):
        if raw_value := self._get_raw_setting_value_from_env(name):
            return _load(raw_value)

    def _get_raw_setting_value_from_env(self, setting_name):
        try:
            return os.environ[setting_name]
        except KeyError:
            return self._handle_missing_setting(setting_name)

    def _handle_missing_setting(self, setting_name):
        if self.cringe_toml.exception_on_missing_setting:
            raise MissingSettingError(setting_name)


def _load(raw_value):
    try:
        return json.loads(raw_value)
    except json.decoder.JSONDecodeError:
        return raw_value
    except IndexError:
        return None
