import bs4
import requests

# Obtengo el archivo HTMl de la página a scrappear
resultado = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")

# Mediante bs4 transformo el contenido HTML en un objeto en el cual puedo filtrar etiquetas y buscar datos
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

titulo_encabezado = sopa.select('title')[0].getText()
parrafo_especial = sopa.select('p')[-1].getText()
columna_lateral = sopa.select('#PopularPosts1 a')
for a in columna_lateral:
    print(a.getText())

print("Titulo del encabezado: ", titulo_encabezado)
print("Parrafo especial: ", parrafo_especial)
