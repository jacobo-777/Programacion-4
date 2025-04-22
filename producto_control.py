from modelo.producto import Producto

class ProductoControl(Producto):
    def __init__(self, nombre: str, precio: float, registro_ica: str, frecuencia_aplicacion: int):
        super().__init__(nombre, precio)
        self.registro_ica = registro_ica  # Usará el setter para validar
        self.frecuencia_aplicacion = frecuencia_aplicacion  # Usará el setter para validar

    @property
    def registro_ica(self):
        return self._registro_ica

    @registro_ica.setter
    def registro_ica(self, valor):
        if not valor:
            raise ValueError("El registro ICA es obligatorio.")
        self._registro_ica = valor

    @property
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, valor):
        if valor <= 0:
            raise ValueError("La frecuencia de aplicación debe ser mayor que cero.")
        self._frecuencia_aplicacion = valor

    def __str__(self):
        return f"{self.nombre} (ICA: {self.registro_ica}, Frecuencia: {self.frecuencia_aplicacion} días) - ${self.precio}"