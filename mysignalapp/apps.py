from django.apps import AppConfig


class MysignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mysignalapp'
    
    
    def ready(self):
        import mysignalapp.signals
       
