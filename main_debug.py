from modelo.cliente import Cliente
from modelo.control_plagas import ControlPlagas
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido

# Crear cliente (punto de interrupción sugerido aquí para composición)
cliente1 = Cliente("Juan Pérez", "12345678")

# Crear productos (punto de interrupción para herencia aquí ↓)
producto1 = ControlPlagas("Insecticida X", 20000, "ICA-1234", 15, 30)
producto2 = Antibiotico("Antibiótico A", 50000, 500, "Bovinos")  # Hereda de Producto

# Crear pedido y agregar productos
pedido = Pedido(cliente1)
pedido.agregar_producto(producto1, 2)
pedido.agregar_producto(producto2, 1)

# Finalizar pedido (punto de interrupción aquí para composición)
factura = pedido.finalizar_pedido()

# Imprimir factura (opcional)
print(f"Factura:\nCliente: {factura.cliente.nombre} - Cédula: {factura.cliente.cedula}")
print("Productos comprados:")
for producto, cantidad in factura.productos:
    print(f"{producto.nombre} - Cantidad: {cantidad} - Total: {producto.valor * cantidad}")
print(f"Total a pagar: {factura.total}")

