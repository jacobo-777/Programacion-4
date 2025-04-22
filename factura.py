
from datetime import datetime

class Factura:
    def __init__(self, cliente, productos):
        self._cliente = cliente
        self._productos = productos
        self._fecha = datetime.now()
        self._total = sum(p.valor * c for p, c in productos)

    @property
    def cliente(self):
        return self._cliente

    @property
    def productos(self):
        return self._productos

    @property
    def fecha(self):
        return self._fecha

    @property
    def total(self):
        return self._total

    def __str__(self):
        return f"Factura de {self.cliente.nombre} - Total: ${self.total:.2f}"