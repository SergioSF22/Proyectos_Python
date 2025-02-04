"""Implementa para la siguiente función cociente(), un manejador de errores:

Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"

Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"

En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división)"""


def cociente(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")


cociente(5, 5)
cociente(5, 'a')
cociente(5, 0)
