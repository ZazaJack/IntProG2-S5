dia = int(input("Ingrese un número del 1 al 7: "))

while dia != 0:
    if dia == 1:
     print("Lunes")
    elif dia == 2:
        print("Martes")
    elif dia == 3:
        print("Miércoles")
    elif dia == 4:
        print("Jueves")
    elif dia == 5:
        print("Viernes")
    elif dia == 6:
        print("Sábado")
    elif dia == 7:
        print("Domingo")
    else:
        print("Número inválido. Debe estar entre 1 y 7.")
    