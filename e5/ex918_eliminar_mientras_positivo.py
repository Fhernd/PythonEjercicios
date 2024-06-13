# Ejercicio 918: Eliminar números positivos desde una colección mientras se cumpla un predicado.

from itertools import dropwhile

numeros = [2, 3, 5, 7, -2, 3, 11, 19, -5, -13]

print(numeros)

print()

resultado = list(dropwhile(lambda n: n >= 0, numeros))

print(resultado)
