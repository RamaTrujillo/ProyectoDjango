from django.shortcuts import render, HttpResponse
from appservicios.models import Servicio

def home(request):
    return render(request, 'home.html')

def servicios(request):
     serv=Servicio.objects.all()
     return render(request, 'servicios.html', {"servicios":serv})

def tienda(request):
     return render(request, 'tienda.html')

def blog(request):
     return render(request, 'blog.html')

def contacto(request):
     return render(request, 'contacto.html')


# Create your views here.
