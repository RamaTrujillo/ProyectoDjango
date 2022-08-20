from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacto, name="contacto"),
    path('google.com', views.contacto, name="valido")
]