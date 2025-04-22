
calificacion1 = int(input("Ingrese la calificación del estudiante 1: "))
calificacion2 = int(input("Ingrese la calificación del estudiante 2: "))
calificacion3 = int(input("Ingrese la calificación del estudiante 3: "))

suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3

print(f"""Calfificaión 1: {calificacion1:>3}
Calificación 2: {calificacion2:>3}
Calificacion 3: {calificacion3:>3}      
{"Promedio:":<15} {promedio:>3.0f}""")