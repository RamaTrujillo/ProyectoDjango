from django.shortcuts import render
from .models import Producto



def tienda(request):
     lista=Producto.objects.all()
     return render(request, 'tienda.html', {"productos":lista})







# Create your views here.
