import os

config_default = (
    'DJANGO_SETTINGS_MODULE',
    'papamana_django.config.settings'
)


def updateconfig(config, env: dict) -> None:
    """
        Function for update config
        config: path settings
        kwargs: environtment
        Example args for update config:
        {
            "HELLO": "test",
            "KAFKA": "127.0.0.1"
        }
    """
    for attr, val in env.items():
        setattr(config, attr, val)
    return
