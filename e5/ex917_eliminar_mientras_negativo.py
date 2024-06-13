# Ejercicio 917: Eliminar números negativos de una colección mientras se cumpla una condición (usar función nombrada).

from itertools import dropwhile

numeros = [-4, -3, -2, -1, 0, 1, -7, 2, 3, 4, 5]

print(numeros)

print()

def eliminar_negativos(n):
    return n < 0

resultado = list(dropwhile(eliminar_negativos, numeros))

print(resultado)
