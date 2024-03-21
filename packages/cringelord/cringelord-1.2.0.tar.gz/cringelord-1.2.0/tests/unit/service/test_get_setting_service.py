import json

import pytest

from cringelord.service import GetSettingService
from cringelord.service.exceptions import MissingSettingError
from cringelord.service.models import CringeTOML, CringeEnvironment


class TestGetSettingService:
    class TestCreation:
        def test(self):
            cringe_toml = CringeTOML(
                config_file="cringe-config.yaml",
                mode="ALL",
                environments={
                    "production": [
                        CringeEnvironment(description="prod", aliases=["prd"])
                    ]
                },
                exception_on_missing_setting=False
            )

            GetSettingService(cringe_toml)

    class TestGetSetting:
        @pytest.mark.parametrize(
            "expected_value",
            [
                "my_value",
                1,
                1.234,
                True,
                [1, 2, 3],
                {"one": 1, "two": 2}
            ]
        )
        def test_existing(self, monkeypatch, expected_value):
            monkeypatch.setenv("MY_SETTING", json.dumps(expected_value))

            cringe_toml = CringeTOML(
                config_file="cringe-config.yaml",
                mode="ALL",
                environments={
                    "production": [
                        CringeEnvironment(description="prod", aliases=["prd"])
                    ]
                },
                exception_on_missing_setting=False
            )

            service = GetSettingService(cringe_toml)

            assert service.get_setting("MY_SETTING") == expected_value

        def test_non_existing_no_exception(self):
            cringe_toml = CringeTOML(
                config_file="cringe-config.yaml",
                mode="ALL",
                environments={
                    "production": [
                        CringeEnvironment(description="prod", aliases=["prd"])
                    ]
                },
                exception_on_missing_setting=False
            )

            service = GetSettingService(cringe_toml)

            assert service.get_setting("does_not_exist") is None

        def test_non_existing_exception(self):
            cringe_toml = CringeTOML(
                config_file="cringe-config.yaml",
                mode="ALL",
                environments={
                    "production": [
                        CringeEnvironment(description="prod", aliases=["prd"])
                    ]
                }
            )

            service = GetSettingService(cringe_toml)

            with pytest.raises(MissingSettingError):
                service.get_setting("does_not_exist")
