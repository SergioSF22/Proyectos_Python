"""Implementa y crea una ruta absoluta que nos permita llegar al archivo "117.py"
Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario."""
from pathlib import Path

base = Path.home()
ruta = Path(base , "/Desktop/Curso_Python/Recetario/ejercicios/ej117.py")
print(ruta)