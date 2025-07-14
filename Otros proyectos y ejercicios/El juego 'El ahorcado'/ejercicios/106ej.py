"""Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan,
 y devuelva esa cantidad como resultado.
"""
def cantidad_atributos(*args):
    return len(args)

print(cantidad_atributos(2,3,4,5,6,7))