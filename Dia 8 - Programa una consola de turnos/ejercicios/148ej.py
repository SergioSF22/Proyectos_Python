"""Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next."""


def generar_numeros():
    num = 0
    while True:
        num += 1
        yield num


g = generar_numeros()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
