from django import forms  #creo el formulario con django

class formulario(forms.Form):

    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.EmailField(label="E-mail", required=True)
    asunto=forms.CharField(label="Asunto")
    contenido=forms.CharField(label="Mensaje", required=True, widget=forms.Textarea)

