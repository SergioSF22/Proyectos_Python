# Importación de librerias necesarias
import cv2
import face_recognition as fr
import os
import numpy as np
from datetime import datetime

# Creamos las variables para nuestra BBDD
ruta = '..\\recursos\\Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)
# Recorremos las fotos de nuestros empleados almacenando cada imagen y nombre del empleado por separado
for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}\\{nombre}")
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


# Función que codifica las imagenes pasadas por parámetro
def codificar(imagenes):
    # Creamos una nueva lista para las imagenes codificadas
    lista_codificada = []

    # Itera sobre las imagenes pasadas por parámetro
    for imagen in imagenes:
        # Pasamos las imagenes de BGR a RGB
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        # Codificar la imagen
        codificado = fr.face_encodings(imagen)[0]
        # Agregamos a la lista de imagenes codificadas
        lista_codificada.append(codificado)

    # Devolvemos la lista con las imagenes codificadas
    return lista_codificada


# Función que registra los ingresos de los empleados
def registrar_ingresos(persona):
    # Abre el archivo 'registro.csv' para insertar el ingreso de la persona capturada
    with open('registro.csv', 'r+') as f:
        lista_datos = f.readlines()
        nombres_registro = []
        # Lee el archivo para guardar todos los nombres de los empleados ya registrado en el dia de hoy
        for linea in lista_datos:
            ingreso = linea.split(',')
            nombres_registro.append(ingreso[0])
        # Si el empleado reconocido no ha sido registrado con anterioridad, lo registra junto con la hora actual
        if persona not in nombres_registro:
            ahora = datetime.now()
            string_ahora = ahora.strftime('%H:%M:%S')
            f.writelines(f"\n{persona},{string_ahora}")


# Obtiene las imagenes de los empleados codificadas
lista_empleados_codificada = codificar(mis_imagenes)

# Captura una imagen de nuestra cámara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Lee la imagen capturada
exito, imagen = captura.read()

if not exito:
    print("No se ha podido realizar la captura")
else:
    # Reconoce cara en la captura
    cara_captura = fr.face_locations(imagen)
    # Codifica la cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    # Busca coincidencias entre la cara capturada y nuestra BBDD
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        print(distancias)
        indice_coincidencia = np.argmin(distancias)
        # Mostrar coincidencias si las hay
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")
        else:
            # Busca el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]
            # Almacena las coordenadas de la cara capturada
            y1, x2, y2, x1 = caraubic
            # Muestra un rectángulo y el nombre del empleado en las coordenadas de la cara capturada
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 20), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)
            # Registra el ingreso de la persona capturada
            registrar_ingresos(nombre)
            # Mostrar la imagen obtenida
            cv2.imshow('Imagen webcam', imagen)
            # Mantiene la ventana abierta
            cv2.waitKey(0)
            print(f"Bienvenido al trabajo {nombre}")
