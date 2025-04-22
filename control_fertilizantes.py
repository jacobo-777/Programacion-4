
from .producto import Producto

class ControlFertilizantes(Producto):
    def __init__(self, nombre: str, valor: float, componente: str, presentacion: str):
        super().__init__(nombre, valor)
        self._componente = componente
        self._presentacion = presentacion

    @property
    def componente(self):
        return self._componente

    @componente.setter
    def componente(self, value):
        self._componente = value

    @property
    def presentacion(self):
        return self._presentacion

    @presentacion.setter
    def presentacion(self, value):
        self._presentacion = value

    def __str__(self):
        return f"{self.nombre} - Componente: {self.componente} - Presentación: {self.presentacion} - ${self.valor}"

