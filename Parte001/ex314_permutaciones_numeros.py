# Ejercicio 314: Generar las permutaciones para una lista de 3 valores numéricos.

from itertools import permutations

numeros = [1, 2, 3]

permutaciones = list(permutations(numeros))

print(permutaciones)
