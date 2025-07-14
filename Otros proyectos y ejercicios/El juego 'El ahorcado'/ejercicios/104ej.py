"""Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
"""


def suma_absolutos(*args):
    suma = 0
    for n in args:
        suma += abs(n)
    return suma


print(suma_absolutos(5, -9, 2, -5, -1))
