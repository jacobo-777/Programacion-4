
class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self._nombre = nombre
        self._cedula = cedula

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    def __str__(self):
        return f"{self.nombre} - C.C. {self.cedula}"
