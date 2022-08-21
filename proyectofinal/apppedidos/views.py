from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Pedidos, LineaPedido
from appcarrito.carrito import Carrito
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


@login_required(login_url="appautenticacion/login")
def procesar_pedido(request):
    pedido=Pedidos.objects.create(user=request.user)
    carro=Carrito(request)
    lineas_pedido=list()
    for key, value in carro.carrito.items(): #rescato la info y creo el pedido
        lineas_pedido.append(LineaPedido(
            user=request.user,
            producto_id=key,
            cantidad=value["cantidad"],
            pedido=pedido
            ))
        carro.quitar_stock(key, value["cantidad"])

    LineaPedido.objects.bulk_create(lineas_pedido) #hace varios inserts to

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        emailusuario=request.user.email,
    )

    messages.success(request, "El pedido se creo correctamente.")

    return redirect("../tienda")

def enviar_mail(**kwargs):
    asunto="Gracias por tu pedido!"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido":kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombre_usuario":kwargs.get("nombreusuario")

    })

    mensaje_texto=strip_tags(mensaje)

    from_email="email" ##cuenta de email
    to=kwargs.get("emailusuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)




