"""Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
"""


class Personaje:
    def __init__(self, cant_flechas):
        self.cantidad_flechas = cant_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas -= 1

arquero = Personaje(6)
arquero.lanzar_flecha()
print(arquero.cantidad_flechas)
