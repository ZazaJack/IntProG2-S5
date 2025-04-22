
cantidad_inicial_inventario = int(input("Ingrese la cantidad inicial de inventario: "))
cantidad_productos_recibididos = int(input("Ingrese la cantidad de productos recibidos: "))
cantidad_inicial_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))

Suma  = cantidad_inicial_inventario + cantidad_productos_recibididos 
inventario_actual = Suma - cantidad_inicial_vendidos

print(f"Cantidad inicial de inventario: {cantidad_inicial_inventario}")
print(f"Cantidad de productos recibidos: {cantidad_productos_recibididos}")
print(f"Cantidad de productos vendidos: {cantidad_inicial_vendidos}")

print(f"Inventario actual: {inventario_actual}")
print(f"Cantidad de productos en inventario: {Suma}")

 
