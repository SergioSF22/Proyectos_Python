def generador_perfumeria():
    turno = 1
    while True:
        yield f"P-{turno}"
        turno += 1


def generador_farmacia():
    turno = 1
    while True:
        yield f"F-{turno}"
        turno += 1


def generador_cosmetica():
    turno = 1
    while True:
        yield f"C-{turno}"
        turno += 1


p = generador_perfumeria()
f = generador_farmacia()
c = generador_cosmetica()


def decorador(seccion):
    print('*' * 23)
    print("Su turno es: ")
    if seccion == 'P':
        print(next(p))
    elif seccion == 'F':
        print(next(f))
    else:
        print(next(c))
    print("Espere a ser atendido")
    print('*' * 23)

