"""Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"""""
def sobrescribir(nombre_archivo):
    archivo = open(nombre_archivo, 'w')
    archivo.write("Contenido eliminado")
    archivo.close()

sobrescribir('ejemplo.txt')