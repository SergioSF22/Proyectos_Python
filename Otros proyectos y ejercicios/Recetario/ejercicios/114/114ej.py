"""Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar."""
archivo = open('registro.txt', 'a')
registro_ultima_sesion = ["\nFederico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
for p in registro_ultima_sesion:
    archivo.writelines(p + "\t")
archivo.close()

archivo = open('registro.txt', 'r')
for l in archivo:
    print(l)
archivo.close()
