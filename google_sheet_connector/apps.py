from django.apps import AppConfig


class GoogleSheetConnectorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'google_sheet_connector'
    verbose_name = 'Google Sheet API Connector'
