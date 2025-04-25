
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos en el mes: "))
cantidad_personas = int(input("Ingrese la cantidad de personas que habitan en la casa: "))

consumo_mensual = litros_consumidos / cantidad_personas

consumo_diario_por_persona = consumo_mensual / 30

print(f"Los litros consumidos en el mes son: {litros_consumidos} litros")
print(f"La cantidad de personas que habitan en la casa son: {cantidad_personas} personas")
print(f"El consumo mensual por persona es de: {consumo_mensual:.2f} litros")
print(f"El consumo diario por persona es de: {consumo_diario_por_persona:.2f} litros")


