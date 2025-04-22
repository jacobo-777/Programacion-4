
class Producto:
    def __init__(self, nombre: str, valor: float):
        self._nombre = nombre
        self._valor = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    def __str__(self):
        return f"{self._nombre} - ${self._valor}"
