# Ejercicio 958: Usar las funciones chain() y zip_longest() para fusionar listas de diferente tamaño (longitud).

from itertools import chain, zip_longest

primos = [2, 3, 5, 7]
letras = ['A', 'B', 'C']
negativos = [-1, -2]
reales = [3.14, 2.71, 1.41, 0.73, 0.91]

# [2, 'A', -1, 3.14, 3, 'B', -2, 2.71, ...]

resultado = [e for e in chain(*zip_longest(primos, letras, negativos, reales)) if e is not None]

print(resultado)
