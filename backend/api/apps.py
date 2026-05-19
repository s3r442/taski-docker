"""App config for the API application."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration for the api Django app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
