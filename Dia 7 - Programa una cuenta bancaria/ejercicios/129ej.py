"""Crea una instancia de la clase Alarma, que tenga un método llamado posponer(cantidad_minutos). El método debe imprimir en pantalla el mensaje

"La alarma ha sido pospuesta {cantidad_minutos} minutos"""""


class Alarma:
    def posponer(self, minutos):
        print(f"La alarma ha sido pospuesta {minutos} minutos")

mi_alarma = Alarma()
mi_alarma.posponer(25)