from django.contrib import admin
from pagesApp.models import Pagina
# Register your models here.

#Mostrar campos ocultos del modelo 
class PaginaAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at')
    search_fields = ('title','content')
    list_filter = ('visible',)
    list_display = ('title','visible','created_at')
    ordering = ('created_at',)
    
#Agregar mi modelo a la pagina admin
admin.site.register(Pagina,PaginaAdmin)

#Cambiando el nombre del panel de administracion que viene por defecto
#Titulo de la cabecera de la pagina
admin.site.site_header = "Proyecto Blog"

#Titulo en la pestaña del navegador
admin.site.site_title = "Blog"

#Titulo menu opciones
admin.site.index_title = "Inicio - Blog"
