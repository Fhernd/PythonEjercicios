# Ejercicio 916: Eliminar números negativos de una colección mientras se cumpla una condición.

from itertools import dropwhile

numeros = [-4, -3, -2, -1, 0, 1, -7, 2, 3, 4, 5]

print(numeros)

resultado = list(dropwhile(lambda n: n < 0, numeros))

print(resultado)
