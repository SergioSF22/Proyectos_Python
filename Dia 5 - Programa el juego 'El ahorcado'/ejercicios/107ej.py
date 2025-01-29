"""Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo."""
def lista_atributos(**kwargs):
    return list(kwargs.items())

print(lista_atributos(nombre="paco",edad=34))