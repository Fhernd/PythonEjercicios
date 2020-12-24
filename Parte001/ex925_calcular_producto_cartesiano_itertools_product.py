# Ejercicio 925: Calcular el producto cartesiano de dos listas con la función product() de itertools.

from itertools import product

numeros = [[1, 2], [3, 4]]

# [1, 2] x [3, 4] = [(1, 3), (1, 4), (2, 3), (2, 4)]

print(numeros)

print()

resultado = list(product(*numeros))
print(resultado)

print()

resultado = list(product([], [11, 13]))
print(resultado)
