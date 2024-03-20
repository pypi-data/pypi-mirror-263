from pathlib import Path

from cringelord.service.models import CringeEnvironment, CringeMode, CringeTOML


class TestCringeTOML:
    class TestCreation:
        def test(self, cringe_env, abs_config_path):
            CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={"production": [cringe_env]},
                src_dir=Path.cwd(),
                default_environment="production",
                templates=[Path.cwd()]
            )

        def test_with_cringe_mode(self, cringe_env, rel_config_path):
            CringeTOML(
                config_file=rel_config_path,
                mode=CringeMode.ALL,
                environments={"production": [cringe_env]},
                src_dir=Path.cwd(),
                default_environment="production",
                templates=[Path.cwd()]
            )

    class TestPathResolving:
        def test_absolute(self, cringe_env, abs_config_path):
            CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={"production": [cringe_env]}
            )

        def test_relative(self, cringe_env, rel_config_path):
            CringeTOML(
                config_file=rel_config_path,
                mode="ALL",
                environments={"production": [cringe_env]}
            )

    class TestSRCDir:
        def test_mode_all_without_src_dir(
            self,
            cringe_env,
            abs_config_path,
        ):
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={"production": [cringe_env]}
            )

            assert toml.src_dir == Path.cwd()

        def test_mode_all_with_src_dir(
            self,
            cringe_env,
            abs_config_path,
            tmp_path
        ):
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={"production": [cringe_env]},
                src_dir=tmp_path
            )

            assert toml.src_dir == tmp_path

        def test_mode_src_without_src_dir(
            self,
            cringe_env,
            abs_config_path,
        ):
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="SRC",
                environments={"production": [cringe_env]}
            )

            assert toml.src_dir == Path.cwd()

        def test_mode_src_with_src_dir(
            self,
            cringe_env,
            abs_config_path,
            tmp_path
        ):
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="SRC",
                environments={"production": [cringe_env]},
                src_dir=tmp_path
            )

            assert toml.src_dir == tmp_path

    class TestGetEnvironment:
        def test(self, abs_config_path):
            env1 = CringeEnvironment(
                description="Production environment",
                aliases=["prod", "prd"]
            )
            env2 = CringeEnvironment(
                description="Acceptance environment",
                aliases=["acc"]
            )
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={
                    "production": [env1],
                    "acceptance": [env2]
                }
            )

            assert toml.get_environment("production") == env1
            assert toml.get_environment("prod") == env1
            assert toml.get_environment("prd") == env1
            assert toml.get_environment("acceptance") == env2
            assert toml.get_environment("acc") == env2

    class TestGetAllEnvironmentNames:
        def test(self, abs_config_path):
            expected_names = ["production", "prod", "prd", "acceptance", "acc"]
            env1 = CringeEnvironment(
                description="Production environment",
                aliases=["prod", "prd"]
            )
            env2 = CringeEnvironment(
                description="Acceptance environment",
                aliases=["acc"]
            )
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={
                    "production": [env1],
                    "acceptance": [env2]
                }
            )

            assert set(toml.get_all_environment_names()) == set(expected_names)

    class TestDefaultEnvironment:
        def test(self, cringe_env, abs_config_path):
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={"production": [cringe_env]},
                default_environment="production",
            )

            assert toml.default_environment == "production"

        def test_not_set(self, abs_config_path):
            env1 = CringeEnvironment(
                description="Production environment",
                aliases=["prod", "prd"]
            )
            env2 = CringeEnvironment(
                description="Acceptance environment",
                aliases=["acc"]
            )
            toml = CringeTOML(
                config_file=abs_config_path,
                mode="ALL",
                environments={
                    "production": [env1],
                    "acceptance": [env2]
                }
            )

            assert toml.default_environment == "production"
