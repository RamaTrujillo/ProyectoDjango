from django.shortcuts import render, HttpResponse
from appservicios.models import Servicio

def home(request):
    return render(request, 'home.html')


def tienda(request):
     return render(request, 'tienda.html')




# Create your views here.
