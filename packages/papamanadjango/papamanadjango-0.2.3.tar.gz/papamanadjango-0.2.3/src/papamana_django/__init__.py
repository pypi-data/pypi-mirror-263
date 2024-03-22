#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import requests as rq
from papamana_django.config.utils import updateconfig
from django.conf import settings as config

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'papamana_django.config.settings')
    
    try:
        url = "https://gist.githubusercontent.com/juandisay/ff74f899c0adc092efe58e704752cc9b/raw/f98c03f8d944815e7429e93fada2eaf8980de348/env.json"
        load_env = rq.get(url)

        updateconfig(
            config,
            load_env.json()
        )
        if load_env.status_code == 200:
            print("Load environtment from network...")
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
