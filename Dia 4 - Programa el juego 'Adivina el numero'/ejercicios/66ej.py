"""Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
"""
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_impares = 0
suma_pares = 0
for num in lista_numeros:
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num

print("Suma pares: ", suma_pares)
print("Suma impares: ", suma_impares)