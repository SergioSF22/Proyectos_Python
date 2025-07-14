"""Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read)."""
def abrir_leer(nombre_archivo):
    archivo = open(nombre_archivo, 'r')
    for linea in archivo:
        print(linea)
    archivo.close()

abrir_leer('114/registro.txt')