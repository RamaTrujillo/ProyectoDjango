from email.headerregistry import ContentDispositionHeader
from django.db import models

class servicios(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=50)
    imagen= models.ImageField(upload_to='servicios')
    created= models.auto_now_add=True
    updated= models.auto_now_add=True

    class Meta:
        verbose_name= 'servicio'
        verbose_name_plural= 'servicios'  
    def __str__(self):
        return self.titulo


# Create your models here.
