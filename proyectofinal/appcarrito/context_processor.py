from .carrito import Carrito

def importe_total(request):
    carrito=Carrito(request)
    total=0
    if request.user.is_authenticated:
        for key, value in request.session['carrito'].items():
            total=total+(float(value['precio']))
            
    return {"importe_total":total}
