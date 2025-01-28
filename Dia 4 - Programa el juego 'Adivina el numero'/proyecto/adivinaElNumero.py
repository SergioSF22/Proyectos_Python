"""La consigna es esta: el programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
Si el usuario no ha acertado en este primer intento, se le va a volver a pedir que elija otro
número. Y así hasta que gane o hasta que se agoten los ocho intentos.
"""
from random import randint

nombre = input("Introduce tu nombre: ")
print(
    f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")
intentos = 8
intento = 0
respuesta = randint(1, 100)

while intentos > 0:
    print("Intentos restante: ", intentos)
    intento = int(input("Di un número: "))
    if intento < 1 or intento > 100:
        print("Número fuera de rango")
    elif intento < respuesta:
        print("El número es MAYOR al escrito")
    elif intento > respuesta:
        print("El número es MENOR al escrito")
    else:
        intentos -= 1
        print("¡Has acertado!")
        print(f"El número era {respuesta}. Has necesitado {8 - intentos} intentos para averiguarlo")
        break
    intentos -= 1

if respuesta != intento:
    print("Has perdido :(")
    print("La respuesta era: ", respuesta)
