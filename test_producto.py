import unittest
from modelo.producto import Producto

class TestProducto(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.producto = Producto("Producto Genérico", 10000)

    def test_creacion_producto(self):
        """Prueba que un producto se cree correctamente."""
        self.assertEqual(self.producto.nombre, "Producto Genérico")
        self.assertEqual(self.producto.valor, 10000)

    def test_modificar_nombre(self):
        """Prueba que se pueda modificar el nombre del producto."""
        self.producto.nombre = "Nuevo Producto"
        self.assertEqual(self.producto.nombre, "Nuevo Producto")

    def test_modificar_valor(self):
        """Prueba que se pueda modificar el valor del producto."""
        self.producto.valor = 15000
        self.assertEqual(self.producto.valor, 15000)

    def test_str_producto(self):
        """Prueba que el método __str__ devuelva el formato correcto."""
        self.assertEqual(str(self.producto), "Producto Genérico - $10000")

if __name__ == "__main__":
    unittest.main()