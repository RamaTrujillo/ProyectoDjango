from django.db import models
from django.contrib.auth.models import User  #utilizar clase user

class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name="categoria"
        verbose_name_plural="categorias"
    
    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True) #le digo q la suba dentro de media/blog y que si no sube nada, puede quedar en blanco
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)  #le digo que tiene relacion con el post por si se da de baja, que de de baja todo
    categorias=models.ManyToManyField(Categoria) #le digo que dentro de las categorias se alojan varios post.

    class Meta():
        verbose_name="post"

    def __str__(self):
        return self.titulo
        





# Create your models here.
