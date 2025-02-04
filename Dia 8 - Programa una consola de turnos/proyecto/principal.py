import numeros


def preguntar():
    print("Bienvenido a la farmacia")
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            seccion = input("Elija una seccion: ").upper()
            ["P", "F", "C"].index(seccion)
        except ValueError:
            print("Opción no válida")
        else:
            break

    numeros.decorador(seccion)


while True:
    preguntar()
    while True:
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except ValueError:
            print("Opción no válida")
        else:
            break
    if otro_turno == "N":
        print("Gracias por su visita")
        break
