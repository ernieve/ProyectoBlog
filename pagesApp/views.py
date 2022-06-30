from django.shortcuts import render
from pagesApp.models import Pagina
from django.contrib.auth.decorators import login_required
# Create your views here.

#Creare la funcion imprima una sola pagina de la BD
@login_required(login_url='register')
def pagina(request,url_amigable):
    #get() = SELECT * FROM pagesApp_pagina WHERE ...
    consulta = Pagina.objects.get(slug=url_amigable)
    
    return render(request,"pagesApp/pagina.html",{"pagina":consulta})