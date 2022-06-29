from django.contrib import admin
from blogApp.models import *

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('user','created_at','updated_at',)
    
    #Metodo para manipular el comportamiento cuando yo guardo un articulo
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

    
# Register your models here.
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
