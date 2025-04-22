from modelo.producto import Producto

class Antibiotico(Producto):
    def __init__(self, nombre: str, valor: float, dosis: int, tipo_animal: str):
        super().__init__(nombre, valor)
        self._dosis = None
        self._tipo_animal = None
        self.dosis = dosis
        self.tipo_animal = tipo_animal

    @property
    def dosis(self):
        return self._dosis

    @dosis.setter
    def dosis(self, value):
        if value < 400 or value > 600:
            raise ValueError("La dosis debe estar entre 400Kg y 600Kg.")
        self._dosis = value

    @property
    def tipo_animal(self):
        return self._tipo_animal

    @tipo_animal.setter
    def tipo_animal(self, value):
        if value.lower() not in ["bovinos", "caprinos", "porcinos"]:
            raise ValueError("El tipo de animal debe ser Bovinos, Caprinos o Porcinos.")
        self._tipo_animal = value

    def __str__(self):
        return f"{self.nombre} - {self.tipo_animal} ({self.dosis}Kg) - ${self.valor}"
