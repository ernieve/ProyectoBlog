from django.db import reset_queries
from django.shortcuts import render, get_object_or_404
from blogApp.models import *

#Importar la paginacion
from django.core.paginator import Paginator

# Create your views here.
def articulos(request):
    
    #Sacar articulos
    articulos = Article.objects.all()#.order_by('-id') #El ordenamiento de ultimo lo estoy haciendo en la clase meta del modelo
    
    #Usando la libreria de paginacion
    #Paginar articulos
    #El primer campo que le paso es la variable de articulos y el segundo es la cantidad que quiero se muestre
    paginator = Paginator(articulos,3)
    
    # Recorger numero paginas
    page = request.GET.get('page')
    page_articles=paginator.get_page(page)
    
    return render(request,'articulos/listas.html',{'title':'Articulos','articles':page_articles})
    #return render(request,'articulos/listas.html',{'title':'Articulos','articles':articulos})

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