from django.apps import AppConfig

class TravelsAppConfig(AppConfig):
    name = 'app.modules.travels'
    label = 'travels'
    verbose_name = 'Travels'

    def ready(self):
        import app.modules.travels.signals

default_app_config = 'app.modules.travels.TravelsAppConfig'
