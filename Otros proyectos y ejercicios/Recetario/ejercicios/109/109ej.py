"""Abre el archivo texto.txt e imprime su contenido.
"""
mi_archivo = open('texto.txt')

for linea in mi_archivo:
    print(linea)

mi_archivo.close()