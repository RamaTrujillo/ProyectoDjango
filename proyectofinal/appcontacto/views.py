from django.shortcuts import render
from .forms import formulario

def contacto(request):
    formulario_contacto=formulario()
    return render(request, 'contacto.html', {"miform":formulario_contacto})
# Create your views here.
