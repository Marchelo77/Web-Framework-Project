from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'retro_cars.auth_app'
    
    def ready(self):
        import retro_cars.auth_app.signals
        result = super().ready()
        return result
