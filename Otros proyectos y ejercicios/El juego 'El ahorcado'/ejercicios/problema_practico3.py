"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False"""


def cero_seguido(*args):
    anterior = ''
    for n in args:
        if n == 0 and anterior == 0:
            return True
        else:
            anterior = n
    return False


print(cero_seguido(6, 0, 5, 1, 0, 3, 0, 1))
print(cero_seguido(5, 6, 1, 0, 0, 9, 3, 5))
