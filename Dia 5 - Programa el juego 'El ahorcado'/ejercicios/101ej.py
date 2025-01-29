"""Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo."""


def reducir_lista(lista):
    lista.remove(max(lista))
    reduccion = list(set(lista))
    return reduccion


def promedio(lista):
    suma = 0
    for n in lista:
        suma += n

    return suma / len(lista)


lista = [1, 2, 15, 7, 2]
print(promedio(reducir_lista(lista)))
