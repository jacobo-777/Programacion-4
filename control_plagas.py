
from modelo.producto import Producto

class ControlPlagas(Producto):
    def __init__(self, nombre: str, valor: float, registro_ica: str, frecuencia: int, carencia: int):
        super().__init__(nombre, valor)
        self._registro_ica = registro_ica
        self._frecuencia = frecuencia
        self._carencia = carencia

    @property
    def registro_ica(self):
        return self._registro_ica

    @registro_ica.setter
    def registro_ica(self, value):
        self._registro_ica = value

    @property
    def frecuencia(self):
        return self._frecuencia

    @frecuencia.setter
    def frecuencia(self, value):
        self._frecuencia = value

    @property
    def carencia(self):
        return self._carencia

    @carencia.setter
    def carencia(self, value):
        self._carencia = value

    def __str__(self):
        return f"{self.nombre} - Registro ICA: {self.registro_ica} - Frecuencia: {self.frecuencia} días - Carencia: {self.carencia} días - ${self.valor}"
