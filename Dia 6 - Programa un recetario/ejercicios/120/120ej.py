"""Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.
"""
def registro_error(nombre_archivo):
    archivo = open(nombre_archivo, 'a')
    archivo.write("\nse ha registrado un error de ejecucion")
    archivo.close()

registro_error('log_errores.txt')