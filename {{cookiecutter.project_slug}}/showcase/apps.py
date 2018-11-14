from django.apps import AppConfig


class ShowcaseAppConfig(AppConfig):
    name = "showcase"
    verbose_name = "Showcase"

    def ready(self):
        try:
            import showcase.signals  # noqa F401
        except ImportError:
            pass
