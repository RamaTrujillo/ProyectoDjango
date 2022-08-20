from django.contrib import admin
from .models import categoriaProducto, Producto

class adminCatProd(admin.ModelAdmin):
    readonly_fields=("updated", "created")

class adminProd(admin.ModelAdmin):
    readonly_fields=("updated", "created")
    



admin.site.register(categoriaProducto, adminCatProd)
admin.site.register(Producto, adminProd)

# Register your models here.
