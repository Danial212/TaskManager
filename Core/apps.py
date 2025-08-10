from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Core'

    def ready(self) -> None:
        from .signals.handlers import user_registered