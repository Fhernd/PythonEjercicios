# Ejercicio 926: Generar todas las combinaciones con repeticiones de colores con el módulo itertools.

from itertools import combinations_with_replacement

colores = ['Rojo', 'Verde', 'Azul']
print(colores)

print()

print(list(combinations_with_replacement(colores, 1)))

print()

print(list(combinations_with_replacement(colores, 2)))

print()

print(list(combinations_with_replacement(colores, 3)))
