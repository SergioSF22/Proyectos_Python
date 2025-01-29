"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""

def contar_primos(numero):
    primos = 0
    for dividendo in range(numero, 1, -1):
        es_primo = True
        for divisor in range(numero, 1, -1):
            if dividendo % divisor == 0 and dividendo != divisor:
                es_primo = False
                break
        if es_primo:
            primos += 1
    return primos

print(contar_primos(100))