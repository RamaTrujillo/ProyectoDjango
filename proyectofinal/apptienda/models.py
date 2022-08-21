from tkinter import CASCADE
from django.db import models

class categoriaProducto(models.Model):
    categoria=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)

    class Meta():
        verbose_name="categoriaProducto"
        verbose_name_plural="categoriasProducto"
    def __str__(self):
        return self.categoria

class Producto(models.Model):
    nombre=models.CharField(max_length=25)
    categoria=models.ForeignKey(categoriaProducto, on_delete=models.CASCADE)
    imagen=models.ImageField(null=True, blank=True)
    precio=models.FloatField()
    disponibilidad=models.BooleanField()
    stock=models.PositiveIntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    


    class Meta():
        verbose_name="Producto"
        verbose_name_plural="Productos"
    def __str__(self):
        return self.nombre



# Create your models here.
