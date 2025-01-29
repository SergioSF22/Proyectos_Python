"""Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma."""


def suma_menores(lista):
    suma = 0
    for n in lista:
        if 0 < n < 1000:
            suma += n
    return suma


lista_numeros = [32, 45, 1021, -5]
