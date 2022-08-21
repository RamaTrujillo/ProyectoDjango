from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User

class VRegistro(View):
    def get(self, request):
        form=UserCreationForm()
        return render(request, "registro.html", {"form":form})

    def post(self, request): #post para validar el usuario para el registro
        form=UserCreationForm(request.POST)
        if form.is_valid():
            usuario=form.save() #guardo el formulario
            login(request, usuario) #lo paso de parametro para logearlo
            return redirect("home")
        else:
            for i in form.error_messages: #recorro los posibles mensajes de error de la api form
                messages.error(request, form.error_messages[i])

            return render(request, "registro.html", {"form":form})

def cerrar_sesion(request): #cierre de sesión 
    logout(request)
    return redirect("home")

def log(request):
    if request.method=="POST": #si el metodo es post (envia el formulario)
        form=AuthenticationForm(request, data=request.POST) 
        if form.is_valid(): #si es valido(si paso las pruebas)
            nombre_usuario=form.cleaned_data.get("username") #guardo el nombre de usuario
            pw=form.cleaned_data.get("password") #guardo la pass
            usuario=authenticate(username=nombre_usuario, password=pw) #autentico el usuario
            if usuario is not None: #si el usuario no es null
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Usuario No Valido")
        else:
            messages.error(request, "Usuario o contraseña erroneos")

    form=AuthenticationForm()
    return render(request, "login.html", {"form_login":form})


# Create your views here.



        

    

# Create your views here.
