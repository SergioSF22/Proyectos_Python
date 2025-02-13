import requests
import bs4

# Crear una url sin número de página
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# Lista de titulos de libros con 4 o 5 estrellas
high_rating_titles = []

# Iterar páginas de la web
for pagina in range(1,51):
    # Creamos la sopa de texto por cada página
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar sobre los libros
    for l in libros:
        # Comprobar si tiene 4 o 5 estrellas
        if len(l.select('.star-rating.Four')) != 0 or len(l.select('.star-rating.Five')) != 0:
            # Guardar título en una variable
            titulo_libro = l.select('a')[1]['title']
            # Guardamos el título en la lista de títulos
            high_rating_titles.append(titulo_libro)

# Visualizar los libros de 4 o 5 estrellas
for titulo in high_rating_titles:
    print(titulo)
