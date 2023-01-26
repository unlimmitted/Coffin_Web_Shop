from django.apps import AppConfig


class WebappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webapp'

class coffinList_config(AppConfig):
    name = 'webapp'
    verbose_name = 'Менеджмент гробов'
