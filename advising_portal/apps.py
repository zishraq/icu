from django.apps import AppConfig


class AdvisingPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advising_portal'

    def ready(self):
        import advising_portal.signals
