from django.urls import path
from mainApp import views

#Importo las librerias necesarias para usar mis urls de esta app

urlpatterns = [
    path('',views.index,name="index"),
    path('inicio/',views.index,name="inicio"),
    path('registro/',views.register_page, name='register'),
    path('inicio_sesion/',views.login_page, name='inicio_sesion'),
    path('cerrar_sesion/',views.logout_user,name='logout')
]
