from .app import get_cringe_setting

cringe_toml = None


if not cringe_toml:
    from .app import setup_cringelord

    print(f"--- Performing initialization!")
    cringe_toml = setup_cringelord()
