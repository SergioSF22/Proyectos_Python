"""Aplica un Counter (contador) sobre la lista de números entregada a continuación, y almacénalo en una variable llamada contador
"""
from collections import Counter

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)
print(contador)
