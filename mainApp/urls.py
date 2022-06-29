from django.urls import path
from mainApp import views

#Importo las librerias necesarias para usar mis urls de esta app

urlpatterns = [
    path('',views.index,name="index"),
    path('inicio/',views.index,name="inicio"),
]
