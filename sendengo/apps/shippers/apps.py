from django.apps import AppConfig


class ShippersAppConfig(AppConfig):

    name = "sendengo.apps.shippers"
    verbose_name = "Embarcadores"
    
    def ready(self):
        try:
            from sendengo.apps.shippers import signals # noqa F401
        except ImportError:
            pass
