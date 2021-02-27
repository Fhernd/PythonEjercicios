# Ejercicio 979: Usar la función product() de itertools para calcular el producto de cartesiano de dos listas.

from itertools import product

numeros = [[1, 2], [3, 4]]
print(numeros)

print()

# => [(1, 3), (1, 4), (2, 3), (2, 4)]

resultado = list(product(*numeros))
print(resultado)
