class MissingSettingError(Exception):
    msg_template = """
    Your environment doesn't contain the '{}' environment variable.
    """

    def __init__(self, setting_name):
        msg = self.msg_template.format(setting_name)

        super().__init__(msg)
