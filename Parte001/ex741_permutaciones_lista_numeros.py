# Ejercicio 741: Usar itertools.permutations() para crear las permutaciones de una lista de números.

from itertools import permutations

colores = ['Rojo', 'Verde', 'Azul']

permutaciones = list(permutations(colores))

for p in permutaciones:
    print(p)

print('Cantidad de permutaciones: %i' % len(permutaciones))
