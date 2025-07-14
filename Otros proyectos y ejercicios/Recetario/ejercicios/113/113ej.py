"""Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar."""
archivo = open('mi_archivo.txt', 'a')
archivo.write("\nNuevo inicio de sesion")
archivo.close()

archivo = open('mi_archivo.txt', 'r')
for l in archivo:
    print(l)
archivo.close()