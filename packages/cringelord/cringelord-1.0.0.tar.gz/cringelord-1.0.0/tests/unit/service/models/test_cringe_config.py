import pytest

from cringelord.service.models import CringeConfig, EnvNames
from cringelord.service.models.exceptions import (
    MissingSettingError,
    SettingMismatchError
)


class TestCringeConfig:
    def test(self):
        config_dict = {
            "production": {
                "setting1_name": "production_setting1_value",
                "setting2_name": "production_setting2_value"
            },
            "acc": {
                "setting1_name": "acceptance_setting1_value",
                "setting2_name": "acceptance_setting2_value"
            },
            "general_setting1_name": "general_setting1_value",
            "general_setting2_name": "general_setting2_value"
        }
        env_names = EnvNames(
            current_env="production",
            other_envs=["production", "acceptance", "acc"]
        )
        cringe_config = CringeConfig(
            config_dict=config_dict,
            env_names=env_names
        )
        expected_settings = [
            "setting1_name",
            "setting2_name",
            "general_setting1_name",
            "general_setting2_name"
        ]

        actual_settings = cringe_config.get_settings()

        assert set(actual_settings) == set(expected_settings)

    def test_aliases(self):
        config_dict = {
            "production": {
                "setting1_name": "production_setting1_value",
                "setting2_name": "production_setting2_value"
            },
            "acc": {
                "setting1_name": "acceptance_setting1_value",
                "setting2_name": "acceptance_setting2_value"
            },
            "general_setting1_name": "general_setting1_value",
            "general_setting2_name": "general_setting2_value"
        }
        env_names = EnvNames(
            current_env="production",
            other_envs=["acceptance", "acc", "acc", "acc"]
        )
        cringe_config = CringeConfig(
            config_dict=config_dict,
            env_names=env_names
        )
        expected_settings = [
            "setting1_name",
            "setting2_name",
            "general_setting1_name",
            "general_setting2_name"
        ]

        actual_settings = cringe_config.get_settings()

        assert set(actual_settings) == set(expected_settings)

    def test_raises_mismatch(self):
        config_dict = {
            "production": {
                "setting1_name": "production_setting1_value",
                "setting2_name": "production_setting2_value"
            },
            "acc": {
                "setting1_name": "acceptance_setting1_value",
                "setting3_name": "acceptance_setting3_value"
            },
            "general_setting1_name": "general_setting1_value",
            "general_setting2_name": "general_setting2_value"
        }
        env_names = EnvNames(
            current_env="production",
            other_envs=["acceptance", "acc", "acc", "acc"]
        )
        with pytest.raises(SettingMismatchError):
            CringeConfig(
                config_dict=config_dict,
                env_names=env_names
            )

    class TestGetSetting:
        def test(self):
            config_dict = {
                "production": {
                    "setting1_name": "production_setting1_value",
                    "setting2_name": "production_setting2_value"
                },
                "acc": {
                    "setting1_name": "acceptance_setting1_value",
                    "setting2_name": "acceptance_setting2_value"
                },
                "general_setting1_name": "general_setting1_value",
                "general_setting2_name": "general_setting2_value"
            }
            env_names = EnvNames(
                current_env="production",
                other_envs=["acceptance", "acc", "acc", "acc"]
            )
            cringe_config = CringeConfig(
                config_dict=config_dict,
                env_names=env_names
            )
            with pytest.raises(MissingSettingError):
                cringe_config.get_setting("does_not_exist")

            assert cringe_config.get_setting("setting1_name") == "production_setting1_value"
            assert cringe_config.get_setting("general_setting1_name") == "general_setting1_value"
