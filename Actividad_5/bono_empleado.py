bono = 0
sueldo_empleado = float(input("Ingrese el sueldo del empleado: "))
if sueldo_empleado < 3000:
    bono = sueldo_empleado * 0.10
elif sueldo_empleado >= 1500 and sueldo_empleado <= 3000:
    bono = sueldo_empleado * 0.05
elif sueldo_empleado <= 1500:
    print("El empleado no tiene derecho a bono.")
else:
    print("El sueldo ingresado no es válido. Debe ser un número positivo.")


print(f"El bono del empleado es: {bono:.2f}")
print(f"El sueldo del empleado es: {sueldo_empleado:.2f}")
print(f"Salario total del empleado: {sueldo_empleado + bono:.2f}")
