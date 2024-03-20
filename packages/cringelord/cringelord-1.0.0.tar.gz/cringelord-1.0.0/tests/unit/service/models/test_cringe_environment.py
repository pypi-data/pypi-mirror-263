import pydantic
import pytest

from cringelord.service.models.cringe_environment import CringeEnvironment


class TestCringeEnvironment:
    class TestCreation:
        def test(self):
            CringeEnvironment(
                description="test",
                aliases=["1", "2"]
            )

        def test_description(self, cringe_env, env_description):
            expected_description = env_description

            actual_description = cringe_env.description

            assert actual_description == expected_description

        def test_aliases(self, cringe_env, env_aliases):
            expected_aliases = env_aliases

            actual_aliases = cringe_env.aliases

            assert actual_aliases == expected_aliases

        def test_no_aliases(self):
            expected_aliases = []

            env = CringeEnvironment(description="My description")
            actual_aliases = env.aliases

            assert actual_aliases == expected_aliases

        def test_raises_validation_error_without_description(self):
            with pytest.raises(pydantic.ValidationError):
                CringeEnvironment(aliases=["alias1", "alias2"])
