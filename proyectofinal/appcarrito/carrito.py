class Carrito:
    def __init__(self, request):
        self.request=request
        self.session=request.session #confirmo la session
        carrito=self.session.get("carrito")
        if not carrito:
            carrito=self.session["carrito"]={ } #si no hay carro lo creo
        self.carrito=carrito #si habia carro lo dejo como estaba

    def agregar(self, producto):
        if(str(producto.id) not in self.carrito.keys()):
            self.carrito[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else:
            for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()
    
    def guardar_carro(self):
        self.session["carrito"]=self.carrito
        self.session.modified=True

    def eliminar(self, producto):
        producto.id=str(producto.id)
        if producto.id in self.carrito:
            del self.carrito[producto.id]
            self.guardar_carro()
    
    def restar_producto(self, producto):
        for key, value in self.carrito.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro

    def limpiar_carro(self):
        self.session["carrito"]={}
        self.session.modified=True


            

        