from django.contrib import admin
from .models import Categoria, Post

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated',)

class postAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated',)

admin.site.register(Categoria, categoriaAdmin )
admin.site.register(Post, postAdmin)



# Register your models here.
