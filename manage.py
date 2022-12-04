#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import environ


env = environ.Env()

# Take environment variables from .env file
environ.Env.read_env('core/settings/.env')
env = env('ENV')

if env == 'TEST': sys.exit('[!] TEST ENV should not run from manage.py')
settings_module = 'core.settings.dev' if env == 'DEV' else 'core.settings.prod'

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          settings_module)
    try:
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
