from django.db import reset_queries
from django.shortcuts import render, get_object_or_404
from blogApp.models import *

# Create your views here.
def articulos(request):
    articulos = Article.objects.all()#.order_by('-id') #El ordenamiento de ultimo lo estoy haciendo en la clase meta del modelo
    return render(request,'articulos/listas.html',{'title':'Articulos','articles':articulos})

def categoria(request,categoria_id):
    #categoria = Category.objects.get(id=categoria_id)
    #Arrojando error 404 sino consigue el id
    categoria = get_object_or_404(Category, id=categoria_id)
    #Aqui estoy haciendo una consulta buscando los articulos que corresponden a la categoria donde abro la ventana
    articulos = Article.objects.filter(categories=categoria_id)
    #Debo cuidar de enviar el mismo nombre de clave para los articulos ya que estoy reusando la template lista
    return render(request,'categorias/categoria.html',{'categoria':categoria,'articles':articulos})

def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request,'articulos/detalle.html',{'articulo':article})