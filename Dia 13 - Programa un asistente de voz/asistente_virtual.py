# Importación de las librerias a utilizar
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    # Almacenar el reconocedor en una variable
    r = sr.Recognizer()

    # Configuramos el mimcrófono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar del comienzo de la grabación de voz
        print("Ya puedes hablar")

        # Guardar lo que escuche el micrófono
        audio = r.listen(origen)

        try:
            # Transformar el audio en texto mediante el reconocimineto de voz de Google
            solicitud = r.recognize_google(audio, language="es-es")

            # Prueba de que reconocio la voz
            print("Has dicho: " + solicitud)

            # Devolver solicitud
            return solicitud

        # En caso de que no entienda el audio escuchado
        except sr.UnknownValueError:

            # Prueba de que np entendió el audio
            print("No te he entendido")

            # Devolver error
            return "Estoy a la espera"

        except sr.RequestError:
            # Prueba de que np entendió el audio
            print("Servicio no disponible")

            # Devolver error
            return "Estoy a la espera"

        except:
            # Prueba de que np entendió el audio
            print("Error inesperado")

            # Devolver error
            return "Estoy a la espera"


# Función para que el asistente se comunique con nosotros
def hablar(mensaje):
    # Voces instaladas en mi equipo (Windows)
    voz_castellano = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
    voz_ingles = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    # 'Encender' el motor de pyttsx3
    engine = pyttsx3.init()

    # Definimos el idioma que queremos que tenga en función de las voces instaladas en nuestro equipo. Si no se indica establece por defecto la principal del equipo, en mi caso la castellana.
    engine.setProperty('voice', voz_castellano)

    # Pronocia el mensaje pasado por parámetro
    engine.say(mensaje)
    engine.runAndWait()


# Informar del día de la semana
def pedir_dia():
    # Creamos la variable con los datos del dia actual
    dia = datetime.date.today()
    print(dia)

    # Creamos una variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con los nombres de los dias de la semana
    semana = {
        0: 'Lunes',
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo'
    }

    # Decir el día de la semana
    hablar(f"Hoy es {semana[dia_semana]}")


# Informar de la hora actual
def pedir_hora():
    # Creamos una variable con la hora actual
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos"

    # Decir la hora actual
    hablar(hora)


# Función que define un saludo inicial
def saludo_inicial():
    # Crear una variable con datos de la hora actual
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buenos días"
    else:
        momento = "Buenas tardes"

    # Decir saludo
    hablar(f"{momento}, soy Helena, tu asistente personal. Por favor, dime en que puedo ayudarte")


# Función principal del asistente
def realizar_solicitudes():
    # Activamos el saludo inicial
    saludo_inicial()

    # Variable para salir del bucle
    empezar = True

    # Bucle principal
    while empezar:
        # Activamos el micro y guardamos la solicitud en un str
        solicitud = transformar_audio_en_texto().lower()

        # Definimos las funciones de nuestro asistente en función de lo que escuche
        # Abre youtube
        if 'abrir youtube' in solicitud:
            hablar("Por supuesto. Voy a abrir YouTube")
            webbrowser.open("https://www.youtube.com")
            continue
        # Abre nuestro navegador
        elif 'abrir navegador' in solicitud:
            hablar("Por supuesto. Voy a abrir tu navegador")
            webbrowser.open("https://www.google.com")
            continue
        # Dice que día es hoy
        elif 'qué día es hoy' in solicitud:
            pedir_dia()
            continue
        # Dice que hora es
        elif 'qué hora es' in solicitud:
            pedir_hora()
            continue
        # Busca en wikipedia lo que digamos
        elif 'busca en wikipedia' in solicitud:
            hablar("Estoy buscando eso en wikipedia")
            solicitud = solicitud.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(solicitud, sentences=1)
            hablar('Wikipedia dice lo siguiente: ')
            hablar(resultado)
            continue
        # Busca en internet lo que le digamos
        elif 'busca en internet' in solicitud:
            hablar("Estoy en ello")
            solicitud = solicitud.replace('busca en internet', '')
            pywhatkit.search(solicitud)
            hablar(f"Esto es lo que he encontrado sobre {solicitud}")
            continue
        # Reproduce en Youtube la primera ocurrencia de lo que le digamos
        elif 'reproducir' in solicitud:
            hablar("¡Claro! Voy a reproducir el vídeo en YouTube")
            solicitud = solicitud.replace("reproducir", "")
            pywhatkit.playonyt(solicitud)
            continue
        # Cuenta un chiste
        elif 'chiste' in solicitud:
            hablar(pyjokes.get_joke('es'))
            continue
        # Dice el precio actual de las acciones que le digamos y esten definimos en el dict 'cartera'
        elif 'precio de las acciones' in solicitud:
            accion = solicitud.split('de')[-1].strip()
            cartera = {
                'apple': 'AAPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f"el precio actual de {accion} es {precio_actual} dólares estadounidenses")
            except:
                hablar("Perdón, no he encontrado la acción indicada")
            finally:
                continue
        # Se despide de nosotros y acaba el programa
        elif 'adiós' in solicitud:
            hablar("¡Hasta pronto!")
            break


realizar_solicitudes()
