from django.urls import path
from pagesApp import views
#Importo las librerias necesarias para usar mis urls de esta app

urlpatterns = [
        path('pagina/<str:url_amigable>',views.pagina,name="pagina"),
]
