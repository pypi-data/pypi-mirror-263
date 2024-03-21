from cringelord.service.models import EnvNames


class TestEnvNames:
    def test(self):
        current_env = "Production"
        other_envs = ["Acceptance", "Test", "Development"]

        names = EnvNames(
            current_env=current_env,
            other_envs=other_envs
        )

        assert names.current_env == current_env
        assert names.other_envs == other_envs

    def test_duplicate(self):
        current_env = "Production"
        other_envs = ["Production", "Acceptance", "Test", "Development"]

        names = EnvNames(
            current_env=current_env,
            other_envs=other_envs
        )

        assert names.current_env == current_env
        assert names.other_envs == ["Acceptance", "Test", "Development"]
