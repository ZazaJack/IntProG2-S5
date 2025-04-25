
calificacion_estudiante = int(input("Ingrese la calificación del estudiante: "))
if calificacion_estudiante >= 9 and calificacion_estudiante <= 10:
    print("El estudiante ha aprobado el curso con una calificación de A.")
elif calificacion_estudiante >= 7 and calificacion_estudiante <= 8:
    print("El estudiante ha aprobado el curso con una calificación de B.")
elif calificacion_estudiante >= 5 and calificacion_estudiante <= 6:
    print("El estudiante ha aprobado el curso con una calificación de C.")
elif calificacion_estudiante >= 3 and calificacion_estudiante <= 4:
    print("El estudiante ha aprobado el curso con una calificación de D.")
elif calificacion_estudiante >= 0 and calificacion_estudiante <= 2:
    print("El estudiante ha reprobado el curso con una calificación de F.")
else :
    print("La calificación ingresada no es válida. Debe estar entre 0 y 10.")