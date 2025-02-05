"""En una variable llamada minutos, almacena únicamente los minutos de la hora actual.

Por ejemplo, si se ejecutara a las 20:43:17 de la noche, la variable minutos debe almacenar el valor 43"""
from datetime import time

hora = time(20, 43, 17)
minutos = hora.minute
print(minutos)
