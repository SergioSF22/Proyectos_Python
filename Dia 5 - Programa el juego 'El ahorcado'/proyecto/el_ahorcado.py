"""El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida."""
from random import choice
from time import process_time_ns


def elegir_palabra():
    print("Voy a elegir una palabra y tienes que advinarla. Cuentas con 8 vidas")
    palabras = ['python','arma','ordenador','cascos','programacion','manta','armario','impresora','dinosaurio','escuela','almendra']
    return choice(palabras)

def mostrar_guiones(palabra):
    guiones = []
    for i in range(0,len(palabra)):
        guiones.append('_')
    print("Estructura de la palabra: ", guiones)
    return guiones

def verificar_letra(letra):
    if letra.isalpha() and len(letra) == 1:
        return True
    else:
        return False


palabra = elegir_palabra()
guiones = mostrar_guiones(palabra)
incorrectas = set()
vidas = 8

while vidas > 0:
    print("Letra incorrectas: ", incorrectas)
    letra = input("Introduce una letra: ")
    while not verificar_letra(letra):
        print("Letra inválida")
        letra = input("Introduce una letra: ")
    if letra in palabra:
        print("Letra correcta")
        for indice, valor in enumerate(palabra):
            if letra == valor:
                guiones[indice] = letra
        print(guiones)
        if not '_' in guiones:
            print("¡Has ganado!")
            break
    else:
        print("Letra incorrecta")
        incorrectas.add(letra)
        vidas -= 1
        print("Vidas restantes: ", vidas)
        if vidas == 0:
            print("¡Has perdido!")
            break

