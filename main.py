from modelo.cliente import Cliente
from modelo.control_plagas import ControlPlagas
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido


nombre_cliente = input("Ingrese el nombre del cliente: ")
cedula_cliente = input("Ingrese la cédula del cliente: ")
cliente = Cliente(nombre_cliente, cedula_cliente)


pedido = Pedido(cliente)


productos_disponibles = [
    ControlPlagas("Insecticida X", 20000, "ICA-1234", 15, 30),
    ControlPlagas("Fungicida Z", 15000, "ICA-4321", 10, 25),
    Antibiotico("Antibiotico A", 50000, 500, "Bovinos"),
    Antibiotico("Antibiotico B", 45000, 550, "Porcinos")
]


print("\nProductos disponibles:")
for i, prod in enumerate(productos_disponibles, 1):
    print(f"{i}. {prod}")


cantidad_productos = int(input("\n¿Cuantos productos desea agregar al pedido?: "))


for _ in range(cantidad_productos):
    opcion = int(input("Seleccione el numero del producto a agregar: "))
    cantidad = int(input("Cantidad: "))
    pedido.agregar_producto(productos_disponibles[opcion - 1], cantidad)


factura = pedido.finalizar_pedido()

print("DEBUG:", factura)  # ← Puedes poner el punto de interrupción aquí

print(f"\nFactura:\nCliente: {factura.cliente.nombre} - Cedula: {factura.cliente.cedula}")
print("Productos comprados:")
for producto, cantidad in factura.productos:
    print(f"{producto.nombre} - Cantidad: {cantidad} - Total: {producto.valor * cantidad}")
print(f"Total a pagar: {factura.total}")
