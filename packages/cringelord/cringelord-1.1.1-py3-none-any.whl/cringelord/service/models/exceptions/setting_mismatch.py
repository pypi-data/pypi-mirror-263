class SettingMismatchError(Exception):
    msg_template = "{env1} does not contain the same settings as {env2}."

    def __init__(self, env1_name, env2_name):
        msg = self.msg_template.format(
            env1=env1_name,
            env2=env2_name
        )

        super().__init__(msg)
