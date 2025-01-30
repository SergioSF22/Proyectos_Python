"""Abre el archivo texto.txt e imprime únicamente la segunda línea."""
archivo = open('texto.txt')

lineas = archivo.readlines()
print(lineas[1])

archivo.close()