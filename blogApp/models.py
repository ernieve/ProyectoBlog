from distutils.command.upload import upload
from unicodedata import category
from django.db import models
#Importar el editor de texto enriquecido, luego de haberlo instalado (pip install django-ckeditor)
from ckeditor.fields import RichTextField

#Importar modelos de usuarios para pode relacionarlos
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100,verbose_name='Nombre')
    description=models.CharField(max_length=255,verbose_name='descripcion')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        
    def __str__(self):
        return self.name
    
class Article(models.Model):
    title=models.CharField(max_length=150,verbose_name='Titulo')
    content=RichTextField(verbose_name='Contenido')
    image = models.ImageField(default='null',verbose_name='Imagen',upload_to='articulos')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    updated_at=models.DateTimeField(auto_now=True,verbose_name='Editado el')
    #Aqui creo relacion, osea FK, con el modelo de usuarios. El cascade borrara todos los articulos si es usuario es eliminado, es decir, no habra ER
    #El editable es para evitar que al crear un articulo los usuarios no puedan asignarlos a otros y se relacionen directamente a quien los crea
    user = models.ForeignKey(User, verbose_name='Usuario',on_delete=models.CASCADE, editable=False)
    #Relacion con categorias, el ManyToMany quieres decir que muchos articulos pueden tenes muchas categorias,blank que puede estar vacio
    categories = models.ManyToManyField(Category,verbose_name='Categorias', blank=True)
    
    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'
        ordering=['-created_at']
        
    def __str__(self):
        return self.title