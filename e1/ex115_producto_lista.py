# Ejercicio 115: Calcular el producto de los elementos de una lista sin usar un ciclo for.

from functools import reduce

numeros = [2, 7, 9]

producto = reduce(lambda x, y: x * y, numeros)

print(producto)

numeros = [1, 2, 3, 4, 5]

producto = reduce(lambda x, y: x * y, numeros)

print(producto)
