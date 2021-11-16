from django.apps import AppConfig


class AccountsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog.accounts_app'

    def ready(self):
        import blog.accounts_app.signals
