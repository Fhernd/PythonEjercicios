# Ejercicio 163: Generar combinaciones a través del módulo itertools.

from itertools import combinations

numeros = [2, 3, 5, 7, 11, 13]

for c in combinations(numeros, 3):
    print(c)
