import os
from django.conf import settings as config

config_default = (
    'DJANGO_SETTINGS_MODULE',
    'papamana_django.config.settings'
)


def updateconfig(kwargs: dict) -> None:
    """
        Function for update config
        Example args for update config:
        {
            "HELLO": "test",
            "KAFKA": "127.0.0.1"
        }
    """
    for attr, val in kwargs.items():
        setattr(config, attr, val)
    return
