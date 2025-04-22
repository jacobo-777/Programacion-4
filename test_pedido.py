import unittest
from modelo.pedido import Pedido
from modelo.cliente import Cliente
from modelo.control_plagas import ControlPlagas
from modelo.antibiotico import Antibiotico

class TestPedido(unittest.TestCase):

    def setUp(self):
        # Crear cliente
        self.cliente = Cliente("Carlos", "123456789")

        # Crear productos de prueba
        self.producto1 = ControlPlagas("Insecticida X", 20000, "ICA-1234", 15, 30)
        self.producto2 = Antibiotico("Antibiótico A", 50000, 500, "Bovinos")

        # Crear un pedido
        self.pedido = Pedido(self.cliente)

    def test_agregar_producto(self):
        # Agregar productos al pedido
        self.pedido.agregar_producto(self.producto1, 2)
        self.pedido.agregar_producto(self.producto2, 1)

        # Verificar el total del pedido
        self.assertEqual(self.pedido.total, 90000)  # 2 Insecticida X + 1 Antibiótico A

    def test_finalizar_pedido(self):
        # Agregar productos al pedido
        self.pedido.agregar_producto(self.producto1, 2)
        self.pedido.agregar_producto(self.producto2, 1)

        # Finalizar el pedido y obtener la factura
        factura = self.pedido.finalizar_pedido()

        # Verificar que la factura contenga los productos correctos
        self.assertEqual(len(factura.productos), 2)  # Debe tener 2 productos

        # Verificar que el total de la factura es correcto
        self.assertEqual(factura.total, 90000)  # 2 Insecticida X + 1 Antibiótico A

if __name__ == '__main__':
    unittest.main()
