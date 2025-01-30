"""Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código"""
archivo = open('texto.txt')
print(archivo.readline())
archivo.close()
