from django.urls import path
from blogApp import views

#Importo las librerias necesarias para usar mis urls de esta app

urlpatterns = [
    path('articulos/',views.articulos,name="articulos"),
    path('categoria/<int:categoria_id>',views.categoria,name="categoria"),
    path('articulo/<int:article_id>',views.article,name="articulo"),
]
