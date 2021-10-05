import uuid


class Venta():
    def __init__(self,empleado,cliente,listaCompra,listaCantidades,listaPrecios,total):
        self.codigoVenta= uuid.uuid4()
        self.empleado=  empleado
        self.cliente= cliente
        self.listaCompra= listaCompra
        self.listaCantidades= listaCantidades
        self.listaPrecios= listaPrecios
        self.total= total


    def __repr__(self):
        representacion= "El empleado que realizo la venta es :"+" "+self.empleado.nombre+"\n"+"" \
                        "El cliente que realizo la compra es:"+" "+self.cliente.nombre+"\n"+""
        for i in range(len(self.listaCompra)):
                 representacion= representacion+"Producto:"+" "+str(self.listaCompra[i])+"\n"+"" \
                 "Cantidad solicitada:"+" "+str(self.listaCantidades[i])+"\n"+""\
                 "Valores:"+" "+str(self.listaPrecios[i])+"\n"+""

        return representacion

