import cv2
import face_recognition as fr

# Cargar imágenes
foto_control = fr.load_image_file("../recursos/FotoA.jpg")
foto_prueba = fr.load_image_file("../recursos/FotoC.jpg")

# Cambiamos el sistema de color de las imagenes de BGR a RGB mediante cv2 para que face_recognition pueda trabajar con ellas
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar la cara control y codificarla
lugar_cara_A = fr.face_locations(foto_control)[0]
cara_codificada_A = fr.face_encodings(foto_control)[0]

# Localizar la cara prueba y codificarla
lugar_cara_B = fr.face_locations(foto_prueba)[0]
cara_codificada_B = fr.face_encodings(foto_prueba)[0]

# Mostramos un rectángulo en las imagenes que contengan las caras reconocidas
cv2.rectangle(foto_control,
              (lugar_cara_A[3], lugar_cara_A[0]),
              (lugar_cara_A[1], lugar_cara_A[2]),
              (0, 0, 255),
              2)

cv2.rectangle(foto_prueba,
              (lugar_cara_B[3], lugar_cara_B[0]),
              (lugar_cara_B[1], lugar_cara_B[2]),
              (0, 0, 255),
              2)

# Realizar comparación entre ambas caras, mediante el parámetro 'tolerance' podemos ampliar el valor de la distancia que determina si dos caras pertenecen a la misma persona (0.6 por defecto)
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B)

# Medida de distancia entre caras (Similitud entre ellas)
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B)

# Mostrar resultado
cv2.putText(foto_prueba,
            f"{resultado} {distancia.round(2)}",
            (50, 50),
            cv2.FONT_HERSHEY_PLAIN,
            2,
            (0, 0, 255),
            2)

# Mostrar imagenes
cv2.imshow('Foto control', foto_control)
cv2.imshow('Foto prueba', foto_prueba)

# Mantener el programa abierto
cv2.waitKey(0)
