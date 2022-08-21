from django.db import models
from django.contrib.auth import get_user_model
from apptienda.models import Producto
from django.db.models import Sum, F, FloatField

UserActive=get_user_model()

class Pedidos(models.Model):
    user=models.ForeignKey(UserActive, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Pedidos"
        verbose_name="Pedido"
        verbose_name_plural="Pedidos"
        ordering=["id"]
    
    @property
    def total(self): #por cada producto (F) saco el total multiplicando por su cantidad
        return self.lineapedido_set.aggregate(
            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"]

    def __str__(self):
        return self.id


class LineaPedido(models.Model):
    user=models.ForeignKey(UserActive, on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedidos, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'
    
    class Meta:
        db_table="LineaPedidos"
        verbose_name="linea pedido"
        verbose_name_plural="linea pedidos"
        ordering=["id"]

# Create your models here.
