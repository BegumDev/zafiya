from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout2'

    def ready(self):
        import checkout2.signals