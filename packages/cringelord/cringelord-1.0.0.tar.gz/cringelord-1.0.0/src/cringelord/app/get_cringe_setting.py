from typing import Any, Optional

from pydantic import validate_call

from cringelord.service import GetSettingService


@validate_call
def get_cringe_setting(name: str) -> Optional[Any]:
    """
    Retrieves a setting's value as a Python object from the environment
        configured by Cringelord.

    If you require the serialized value as-is, you should request it directly
        via 'os.environ["setting_name"]'.

    Args:
        name (str): The name of the setting.

    Returns:
        The setting's value loaded into a Python object.

    Raises:
        MissingConfigValueError: If you're requesting a setting that's not
            present in the environment.
            We chose to raise an exception instead of returning a default
            value, because the writer of the script should be aware that
            (s)he's missing configuration values. This approach, for example,
            clarifies that you've made a typo, preventing nasty bugs.
    """
    from cringelord import cringe_toml

    service = GetSettingService(cringe_toml)

    return service.get_setting(name)
