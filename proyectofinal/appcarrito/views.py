from django.shortcuts import redirect
from .carrito import Carrito
from apptienda.models import Producto

def agregar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carrito=Carrito(request)
    producto=Producto.objects.get(id=producto_id)
    carrito.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request):
    carrito=Carrito(request)
    carrito.limpiar_carro()
    return redirect("tienda")






# Create your views here.
