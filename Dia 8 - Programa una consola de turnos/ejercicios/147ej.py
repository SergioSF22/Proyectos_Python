"""Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():

En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"

En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"

Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"

En todos los casos, al finalizar, imprimir: "Finalizando ejecución"""""


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("Archivo no encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")

abrir_archivo('146ej.py')
abrir_archivo('nombre_inventado')
abrir_archivo(25)
