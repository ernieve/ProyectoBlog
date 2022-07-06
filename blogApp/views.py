from django.db import reset_queries
from django.shortcuts import render, get_object_or_404, redirect
from blogApp.models import *
from django.contrib.auth.decorators import login_required
from .forms import *

from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='inicio_sesion')
def articulos(request):
    #Sacar articulos
    articulos = Article.objects.all()#.order_by('-id') #El ordenamiento de ultimo lo estoy haciendo en la clase meta del modelo
    paginator = Paginator(articulos,3)
    
    # Recorger numero paginas
    page = request.GET.get('page')
    page_articles=paginator.get_page(page)
    
    return render(request,'articulos/listas.html',{'title':'Articulos','articles':page_articles})

@login_required(login_url='inicio_sesion')
def crear_articulos(request):
    #POST 
    if request.method=="POST":
        
        formulario = FormArticulo(request.POST)
        
        if formulario.is_valid():
            
            info_articulo = formulario.cleaned_data
            
            articulo = Article(title = info_articulo["title"],
                            content = info_articulo["content"],
                            user_id = request.user.id)
            articulo.save()
                        
            return redirect("articulos")
        
        else:
            redirect("inicio")
    else:
        formulario_vacio = FormArticulo()
        return render(request,"articulos/form_articulo.html",{'form':formulario_vacio})

def editar_articulo(request,id):
    
    articulo = Article.objects.get(id=id)
    
    if request.method == "POST":
        
        formulario = FormArticulo(request.POST)
        if formulario.is_valid():
            info_articulo = formulario.cleaned_data
            articulo = Article(title = info_articulo["title"],content = info_articulo["content"],user_id = request.user.id)
            articulo.save()
            return redirect('articulos')
    #get
    formulario_vacio = FormArticulo(initial={"title":articulo.title,
                                "content":articulo.content})
    return render(request,"articulos/form_articulo.html",{'form':formulario_vacio})



@login_required(login_url='inicio_sesion')
def delete_articulo(request,id):
    borrar_articulo = Article.objects.get(pk=id)
    borrar_articulo.delete()
    return redirect("articulos")

@login_required(login_url='inicio_sesion')
def categoria(request,categoria_id):
    categoria = get_object_or_404(Category, id=categoria_id)
    articulos = Article.objects.filter(categories=categoria_id)
    return render(request,'categorias/categoria.html',{'categoria':categoria,'articles':articulos})

@login_required(login_url='inicio_sesion')
def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request,'articulos/detalle.html',{'articulo':article})