from difflib import get_close_matches
import os


class MissingSettingError(Exception):
    msg_template = """
    Your environment doesn't contain the '{}' environment variable.
    """

    close_match_msg_template = "Did you mean '{}'?"

    def __init__(self, setting_name):
        msg = self.msg_template.format(setting_name)

        if closest_match := _get_closest_match(setting_name):
            msg += self.close_match_msg_template.format(closest_match)

        super().__init__(msg)


def _get_closest_match(setting_name):
    key_list = list(os.environ.keys())

    close_matches = get_close_matches(setting_name, key_list, n=1, cutoff=0.0)

    try:
        return close_matches[0]
    except IndexError:
        return None
