from django.shortcuts import render
from .models import Servicio

def servicios(request):
     serv=Servicio.objects.all()
     return render(request, 'servicios.html', {"servicios":serv})


# Create your views here.
