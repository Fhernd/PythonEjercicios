# Ejercicio 365: Remover los elementos duplicados de una lista de listas con groupby().

from itertools import groupby

matriz = [[1, 2], [3, 4], [7, 9], [1, 2], [7, 9], [11, 13], [0, 1]]

print(matriz)

matriz.sort()

print(matriz)

resultado = list(lista for lista, _ in groupby(matriz))

print()

print(resultado)
