"""Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:

"Te quedan 3 vidas"

"Te quedan 2 vidas"

"Te queda 1 vida"

"Game Over"

Almacena el generador en la variable perder_vida"""


def restar_vidas():
    vidas = 3
    while vidas > 0:
        if vidas == 1:
            yield f"Te queda {vidas} vida"
        else:
            yield f"Te quedan {vidas} vidas"
        vidas -= 1
    else:
        yield "Game Over"


perder_vida = restar_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
