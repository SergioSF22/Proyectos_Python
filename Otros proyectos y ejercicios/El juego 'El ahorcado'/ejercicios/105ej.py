"""Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}"""""

def numeros_persona(nombre, *args):
    suma = 0
    for n in args:
        suma += n
    return f"{nombre}, la suma de tus números es {suma}"

print(numeros_persona("Sergio", 4, 5, 6, 7, 8))
