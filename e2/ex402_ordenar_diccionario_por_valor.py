# Ejercicio 402: Ordenar un diccionario a partir del valor de los elementos con Counter.

from collections import Counter

productos = {'Teclado': 57.9, 'Monitor': 299.9, 'Mouse': 29.5, 'Deademas': 73.5}

print(productos)

contador = Counter(productos)

print(contador.most_common())
