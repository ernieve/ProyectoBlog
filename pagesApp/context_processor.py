from pagesApp.models import Pagina
#Importo mis modelos para poder usarlos en el context procesor y tener disponibles mis objetos de la bd en cualquier parte del proyecto

#Funcion para obtener paginas, es semejante a crear una vista, para poder usarla en varios sitios
def get_paginas(request):
    #No utilizo el .all() porque seria pesado para el Framework, es mejor usar el .values_list() porque puedo seleccionar el/los elemento(s) que quiero mostrar
    paginas = Pagina.objects.filter(visible=True).order_by('order').values_list('id','title','slug')
    #Asi envio todas la paginas que tenga guardadas en mi BD
    return {
        'paginas': paginas
    }