"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio"""

def devolver_distintos(n1, n2, n3):
    lista = [n1,n2,n3]
    total = sum(lista)
    lista.sort()
    if total > 15:
        return lista[0]
    elif 10 <= total <= 15:
        return lista[1]
    elif total < 10:
        return lista[2]

print(devolver_distintos(3,23,2))