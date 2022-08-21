from django.contrib import admin
from .models import Pedidos, LineaPedido

class adminPedidos(admin.ModelAdmin):
    readonly="created_at"

class adminLineaPedido(admin.ModelAdmin):
    readonly="created_at"
    



admin.site.register(Pedidos, adminPedidos)
admin.site.register(LineaPedido, adminLineaPedido)


# Register your models here.
