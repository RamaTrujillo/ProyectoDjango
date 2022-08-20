from django.urls import path
from proyectoapp import views

urlpatterns = [
    path('', views.home, name="home"),
]