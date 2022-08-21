"""proyectofinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import stat
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #importacion para urlpatterns+= para ver imagenes
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path("servicios/", include('appservicios.urls')),
    path("blog/", include('appblog.urls')),
    path("contacto/", include('appcontacto.urls')),
    path("tienda/", include('apptienda.urls')),
    path("carrito/", include('appcarrito.urls')),
    path("autenticacion/", include('appautenticacion.urls')),
    path("pedidos/", include('apppedidos.urls')),
    path("", include('proyectoapp.urls')),
    
]
urlpatterns+=static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) #url para ver imagenes