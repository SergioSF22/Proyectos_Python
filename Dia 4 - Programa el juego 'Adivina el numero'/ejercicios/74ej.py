"""Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

Llama a la lista obtenida con el nombre de variable lista_indices ."""
cadena = "Python"
lista_indices = list(enumerate(cadena))
print(lista_indices)