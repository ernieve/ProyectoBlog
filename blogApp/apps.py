from django.apps import AppConfig


class BlogappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogApp'

    #Cambiando el nombre en el panel de admin
    verbose_name='Gestión de Blog'