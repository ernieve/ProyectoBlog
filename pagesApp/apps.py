from django.apps import AppConfig


class PagesappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pagesApp'
    
    #Aqui cambio el nombre que se mostrara en la pagina admin
    verbose_name= "Gestión de páginas"
