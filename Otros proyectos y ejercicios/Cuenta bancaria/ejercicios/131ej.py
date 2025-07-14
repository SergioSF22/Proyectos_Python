"""Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez
que es invocado.
El valor predeterminado del atributo vivo, debe ser False."""


class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


jugador1 = Jugador()
jugador1.revivir()
print(jugador1.vivo)
