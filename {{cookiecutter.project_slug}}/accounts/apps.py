from django.apps import AppConfig


class AccountsAppConfig(AppConfig):

    name = 'accounts'
    verbose_name = 'Accounts'

    def ready(self):
        try:
            import accounts.signals  # noqa F401
        except ImportError:
            pass
