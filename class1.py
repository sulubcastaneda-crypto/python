#sistema de venta de un producto
#Creador: Diego Rafael Sulub
#Fecha: 08/06/2026

#Declaracion de constantes
iva = 0.16
Descuento = 0.10

#entrada de datos (I/O)
nombre_cliente = input("Ingrese el nombre del cliente: ")
nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("ingrese el precio unitario del producto: "))
cantidad = int(input("ingrese la cantidad de productos comprados: "))

#calculos
subtotal = precio_unitario * cantidad
monto_descuneto = subtotal * descuento
subtotal_con_descuento = subtotal - monto_descuento
monto_iva = subtotal_con_descuento * iva
total = subtotal_con_descuento + monto_iva

#mostrar tipos de datos con type()
print("\n--- tipos de datos ---")
print("tipos de datos de 'nombre_cliente':", type(nombre_cliente))
print("tipo de dato de 'precio_unitario':", type(precio_unitario))
print("tipo de dato de 'cantidad':",type(cantidad))

#generar ticket de compra
print("\n--- ticket de compra ---")
print("cliente:", nombre_cliente)
print("producto:", nombre_producto)
print("precio unitario: $", precio_unitario)
print("cantidad:", cantidad)
print("-----------------------------")
print("subtotal: $", subtotal)
print("descuento (10%): -$", monto_descuneto)
print("subtotal con descuento: $", subtotal_con_descuento)
print("iva (16%): $", monto_iva)
print("total a pagar: $", total)
print("-----------------------------")
print("¡gracias por su compra")