"""Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función.

Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números."""


def suma(num1, num2):
    try:
        print(num1 + num2)
    except:
        print("Error inesperado")


suma(5, 2)
