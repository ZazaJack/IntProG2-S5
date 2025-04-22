capital_inicial = float(input("Ingrese el capital inicial: "))
tiempo = float(input("Ingrese la cantidad de años: "))
tasa_interes = float(input("Ingrese la tasa de interés: "))

tasa_interes_dec = tasa_interes / 100 
monto_final = ((1 + tasa_interes_dec)**tiempo)*capital_inicial 
interes_ganado = monto_final - capital_inicial

print(f"Capital inicial: {capital_inicial}")
print(f"Tiempo: {tiempo} años")
print(f"Tasa de interés: {tasa_interes}%")
print(f"Monto final: {monto_final:.2f}")
print(f"Interés ganado: {interes_ganado:.2f}")
