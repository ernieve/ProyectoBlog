from django.urls import path
from blogApp import views

#Importo las librerias necesarias para usar mis urls de esta app

urlpatterns = [
    path('articulos/',views.articulos,name="articulos"),
    path('categoria/<int:categoria_id>',views.categoria,name="categoria"),
    path('articulo/<int:article_id>',views.article,name="articulo"),
    path('articulo/crear_articulo/',views.crear_articulos,name='crear_articulo'),
    path('articulo/delete_articulo/<str:id>',views.delete_articulo,name='delete_articulo'),
    path('articulo/editar_articulo/<str:id>', views.editar_articulo, name= "editar_articulo"),
]
