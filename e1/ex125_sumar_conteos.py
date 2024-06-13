# Ejercicio 125: Computar la suma de los conteos de los duplicados de una lista.

from collections import Counter

numeros = [7, 5, 9, 2, 2, 3, 9, 7, 0, 1]

conteos = Counter(numeros)

print(conteos)

print(sum(conteos.values()))
