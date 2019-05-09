from django.apps import AppConfig


class UsersAppConfig(AppConfig):

    name = "sendengo.apps.users"
    verbose_name = "Cuentas"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
