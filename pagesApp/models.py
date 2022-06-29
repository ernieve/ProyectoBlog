from tabnanny import verbose
from django.db import models
#Importar el editor de texto enriquecido, luego de haberlo instalado (pip install django-ckeditor)
from ckeditor.fields import RichTextField

# Create your models here.
class Pagina(models.Model):
    #titulo de la pagina
    title = models.CharField(max_length=50,verbose_name="Titulo")
    #contenido
    #Uso el RichTextField luego de haber instalado, importado la libreria del ckeditor4 y haberlo agregado al settings del proyectos
    content = RichTextField(verbose_name="Contenido")
    #Slug = URL amigables - permite definir una url
    slug = models.CharField(unique=True,max_length=150,verbose_name="Slug")
    #Ordenamiento de las paginas, lo seteo en default 0 para que sea al inicio
    order = models.IntegerField(default=0,verbose_name="Orden")
    #si esta publicado o no
    visible = models.BooleanField(verbose_name="¿Visible?")
    #fecha de creacion
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    #fecha actualizacion
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    
    class Meta:
        verbose_name="Pagina"
        verbose_name_plural="Paginas"
        
    def __str__(self):
        return self.title #para imprimir el titulo en el panel de administracion
