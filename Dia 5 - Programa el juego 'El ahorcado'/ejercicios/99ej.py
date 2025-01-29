"""Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta."""
def cuenta_pares(lista):
    pares = 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
    return pares
