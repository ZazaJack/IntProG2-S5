
litros_precio = 49.57 # Precio del litro de gasolina

distancia_km = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos en el trayecto: "))

división = distancia_km / litros_consumidos


multiplicación = litros_precio * litros_consumidos

print(f"La distancia recorrida es de {distancia_km} km")
print(f"Litros de gasolina consumidos: {litros_consumidos} litros")
print(f"El precio del litro de gasolina es de {litros_precio} pesos")
print(f"El rendimiento del vehículo es de {división:.2f} km/litro")
print(f"El gasto total de gasolina es de {multiplicación:.2f} pesos")