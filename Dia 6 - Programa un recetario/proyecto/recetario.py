import os
from pathlib import Path
from shutil import rmtree

# La carpeta donde realizo todas las operaciones de este programa se encuentra en C:\Users\mi_nombre\Recetas
ruta_recetas = Path(Path.home(), "Recetas")

def mostrar_menu():
    print("""
----------RECETARIO-----------
1. Leer receta
2. Crear receta
3. Crear categoría
4. Eliminar receta
5. Eliminar categoría
6. Salir
------------------------------""")

def mostrar_categorias(ruta_recetas):
    print("-------CATEGORÍAS---------")
    print("Categorias disponibles: ")
    categorias = os.listdir(ruta_recetas)
    for c in categorias:
        print("- ", c)

def mostrar_recetas(ruta_recetas, categoria):
    ruta = Path(ruta_recetas, categoria)
    recetas = os.listdir(ruta)
    print("------RECETAS------")
    for receta in recetas:
        print(receta)

def elegir_categoria():
    categorias = os.listdir(ruta_recetas)
    while True:
        categoria = input("Elige una categoria: ")
        if categoria.capitalize() not in categorias:
            print("Categoría no válida")
        else:
            break
    return categoria

def elegir_receta(categoria):
    recetas = os.listdir(Path(ruta_recetas, categoria))
    while True:
        receta = input("Elige una receta: ")
        if receta not in recetas:
            print("Receta NO válida")
        else:
            break
    return receta


def leer_receta(ruta_receta):
    print("---------RECETA----------")
    receta = open(ruta_receta)
    for linea in receta:
        print(linea)
    receta.close()

def crear_receta(categoria, nombre_receta, contenido_receta):
    ruta = Path(ruta_recetas, categoria, nombre_receta.capitalize())
    nueva_receta = open(ruta, 'w')
    nueva_receta.write(contenido_receta.capitalize())
    nueva_receta.close()
    print("¡Receta creada con exito!")

def crear_categoria(nombre_categoria):
    os.makedirs(Path(ruta_recetas, nombre_categoria))
    print("Categoría creada con éxito")


def eliminar_receta(ruta_receta):
    os.remove(ruta_receta)
    print("¿Receta eliminada!")

def eliminar_categoria(categoria):
    ruta = Path(ruta_recetas, categoria)
    rmtree(ruta)
    print("Categoría eliminada con éxito")

archivos = 0
reinicio = True

print("¡Bienvenido!")
print("La ruta de la carpeta de las Recetas es:", ruta_recetas)
for i in ruta_recetas.glob("**/*.txt"):
    archivos += 1
print(f"Número de recetas actuales: {archivos}")

while reinicio:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    match opcion:
        case '1':
            print("--------LEER RECETA--------")
            mostrar_categorias(ruta_recetas)
            categoria = elegir_categoria()
            mostrar_recetas(ruta_recetas, categoria)
            receta = elegir_receta(categoria)
            ruta_receta = Path(ruta_recetas, categoria, receta)
            leer_receta(ruta_receta)
        case '2':
            print("--------CREAR RECETA--------")
            mostrar_categorias(ruta_recetas)
            categoria = elegir_categoria()
            nombre_nueva_receta = input("Introduce el nombre de tu nueva receta: ") + ".txt"
            contenido_nueva_receta = input("Introduce el contenido de tu nueva receta: ")
            crear_receta(categoria, nombre_nueva_receta, contenido_nueva_receta)
        case '3':
            print("--------CREAR CATEGORÍA--------")
            nueva_categoria = input("Introduce el nombre de la nueva categoría: ")
            crear_categoria(nueva_categoria)
        case '4':
            print("--------ELIMINAR RECETA--------")
            mostrar_categorias(ruta_recetas)
            categoria = elegir_categoria()
            mostrar_recetas(ruta_recetas, categoria)
            receta = elegir_receta(categoria)
            ruta_receta = Path(ruta_recetas, categoria, receta)
            eliminar_receta(ruta_receta)
            pass
        case '5':
            print("--------ELIMINAR CATEGORÍA--------")
            mostrar_categorias(ruta_recetas)
            categoria = elegir_categoria()
            eliminar_categoria(categoria)
            pass
        case '6':
            reinicio = False
        case _:
            print("Opción no válida")
    # os.system('cls')
print("¡Hasta pronto!")
