from django.apps import AppConfig


class RateConfig(AppConfig):
    name = 'rate'

    def ready(self):
        import rate.signals