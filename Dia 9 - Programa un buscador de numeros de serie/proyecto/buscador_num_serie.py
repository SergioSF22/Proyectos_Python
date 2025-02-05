import math
import os
import re
import datetime
import time


def buscar_patron():
    """
    Esta funcion realiza una búsqueda en todas las carpetas y subcarpetas de un
    directorio específico para encontrar archivos de texto que contengan un
    cadena de caracteres que coincida con una expresión regular definida.
    :return: Devuelve una lista  la cual contiene el tiempo de ejecución de la búsqueda
    en su primera posición y un diccionario donde donde las claves son los nombres de
    los ficheros y los valores donde el patron coincidente de cada uno en su segunda posición.
    """
    dicc = {}
    patron = r"N\D{3}-\d{5}"
    ruta = os.getcwd() + "\\Mi_Gran_Directorio"

    inicio = time.time()
    for carpeta, subcarpeta, archivos in os.walk(ruta):
        for arch in archivos:
            txt = open(carpeta + "\\" + arch, 'r')
            contenido = txt.readline()
            coincidencia = re.search(patron, contenido)
            if coincidencia is not None:
                for hallazgo in re.findall(patron, contenido):
                    dicc[arch] = hallazgo
    final = time.time()
    duracion = final - inicio
    return [duracion, dicc]


print('-' * 50)
print("Fecha de búsqueda: ", datetime.date.today().strftime('%d/%m/%Y'))
print("ARCHIVO              Nº SERIE")
print("--------            ----------")
coincidencias = buscar_patron()
for clave, valor in coincidencias[1].items():
    print(f"{clave}\t\t{valor}")
print("\nNúmeros encontrados: ", len(coincidencias[1]))
print(f"Duración de la búsqueda: {math.ceil(coincidencias[0])} segundos")
print('-' * 50)
