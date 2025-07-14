"""Implementa y crea una ruta relativa que nos permita llegar al archivo "
116.py".

Almacena el directorio obtenido en la variable ruta. No olvides importar Path."""
from pathlib import Path

ruta = Path("Curso_Python","Recetario", "ejercicios", "116ej.py")
print(ruta)