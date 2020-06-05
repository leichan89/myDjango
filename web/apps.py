from django.apps import AppConfig

from django.utils.module_loading import import_module


class WebConfig(AppConfig):
    name = 'web'

    def ready(self):
        print("会打印两次")
        import_module("web.signals.web")