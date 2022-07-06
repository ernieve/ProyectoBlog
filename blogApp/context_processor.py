from blogApp.models import Category,Article
#Importo mis modelos para poder usarlos en el context procesor y tener disponibles mis objetos de la bd en cualquier parte del proyecto

#Funcion para obtener paginas, es semejante a crear una vista, para poder usarla en varios sitios
def get_categoria(request):
    #No utilizo el .all() porque seria pesado para el Framework, es mejor usar el .values_list() porque puedo seleccionar el/los elemento(s) que quiero mostrar
    ids_categorias_en_uso = Article.objects.values_list('categories',flat=True)
    categorias = Category.objects.filter(id__in=ids_categorias_en_uso).values_list('id','name')
    #Asi envio todas la paginas que tenga guardadas en mi BD
    return {
        'categorias': categorias,
        'ids': ids_categorias_en_uso
    }