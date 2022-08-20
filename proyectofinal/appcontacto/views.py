from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .forms import formulario

def contacto(request):
    formulario_contacto=formulario()

    if request.method=="POST":
        formulario_contacto=formulario(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            asunto=request.POST.get("asunto")
            contenido=request.POST.get("contenido")
            return redirect('/contacto/?valido')




    return render(request, 'contacto.html', {"miform":formulario_contacto})

# Create your views here.
