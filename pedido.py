
from modelo.factura import Factura

class Pedido:
    def __init__(self, cliente):
        self._cliente = cliente
        self._productos = []
        self._total = 0.0

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, value):
        self._cliente = value

    @property
    def productos(self):
        return self._productos

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    def agregar_producto(self, producto, cantidad):
        self._productos.append((producto, cantidad))
        self._total += producto.valor * cantidad

    def finalizar_pedido(self):
        return Factura(self.cliente, self.productos)
