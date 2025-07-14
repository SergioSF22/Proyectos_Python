# Importamos la librerías que usaremos
import math
import pygame
from pygame import mixer
import random


# Función que establece al jugador en la pantalla
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# Función que establece al enemigo en la pantalla
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))


# Función para disparar las balas
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# Función para detectar coliones
def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distancia < 27:
        return True
    else:
        return False


# Inicializamos Pygame
pygame.init()

# Creamos la pantalla con un tamaño de 800x600 píxeles
pantalla = pygame.display.set_mode((800, 600))

# Cambiamos el título de la ventana y su icono
pygame.display.set_caption("Invasión espacial")
icono = pygame.image.load("../recursos/ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("../recursos/background.jpg")

# Añadimos y reproducimos la música de fondo
mixer.music.load("../recursos/MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)

# Variables con los sonidos del juego
sonido_bala = mixer.Sound("../recursos/disparo.mp3")
sonido_colision = mixer.Sound("../recursos/Golpe.mp3")

# Definimos las variables del jugador como su imagen y sus coordenadas 'x' e 'y' en nuestra pantalla
img_jugador = pygame.image.load("../recursos/nave.png")
jugador_x = 368
jugador_y = 536
jugador_x_cambio = 0

# Definimos las variables de los enemigos como sus imagen y sus coordenadas 'x' e 'y' en nuestra pantalla
img_enemigo = []
posicion = []
enemigo_x, enemigo_y = [], []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("../recursos/enemigo.png"))
    enemigo_x.append(random.randint(0, 731))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# Definimos las variables de las balas como su imagen y sus coordenadas 'x' e 'y' en nuestra pantalla
img_bala = pygame.image.load("../recursos/bala.png")
bala_x = 0
bala_y = 500
bala_y_cambio = 0.5
bala_visible = False

# Definimos la variable de la puntuación
puntuacion = 0
fuente = pygame.font.Font('../recursos/ARCADE_I.TTF', 32)
texto_x = 200
texto_y = 10

# Definimos la variable del texto para finalizar el juego
fuente_final = pygame.font.Font("../recursos/ARCADE_I.TTF", 40)


def mostrar_texto_final():
    mi_fuente_final = fuente_final.render("FIN DEL JUEGO", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (150, 250))


# Función mostrar puntacion
def mostrar_puntuacion(x, y):
    texto = fuente.render(f"PUNTUACION:{puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))


# Bucle que ejecuta el juego
se_ejecuta = True
while se_ejecuta:
    # Definimos el fondo de pantalla
    pantalla.blit(fondo, (0, 0))

    # Bucle que esta a la escucha constante de los eventos del juego
    for evento in pygame.event.get():
        # Si se produce el evento QUIT (Cerrar la ventana) se cambia la variable se_ejecuta para salir del bucle y cerrar el juego
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Captura el evento que corresponde a PULSAR cualquier tecla
        if evento.type == pygame.KEYDOWN:
            # Captura si la tecla pulsada es la flecha izquierda
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            # Captura si la tecla pulsada es la flecha derecha
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            # Captura si pulsamos la tecla espacio
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Captura el evento que corresponde a SOLTAR cualquier tecla
        if evento.type == pygame.KEYUP:
            # Captura si la tecla soltada es la fecla derecha o la flecha izquierda
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificamos la ubicación del jugador
    jugador_x += jugador_x_cambio

    # Condicionales que impiden que la nave traspase los bordes laterales de la pantalla
    if jugador_x <= 5:
        jugador_x = 5
    elif jugador_x >= 731:
        jugador_x = 731

    # Modificamos la ubicación del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            mostrar_texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Condicionales que impiden que el enemigo traspase los bordes laterales de la pantalla y descienda cuando lo haga
        if enemigo_x[e] <= 5:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 731:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        # Detectar colison de la bala
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntuacion += 1
            enemigo_x[e], enemigo_y[e] = random.randint(0, 731), random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    # Actualizamos la posición del jugador y del enemigo
    jugador(jugador_x, jugador_y)

    # Mostrar puntuacion
    mostrar_puntuacion(texto_x, texto_y)

    # Actualizamos la pantalla
    pygame.display.update()
