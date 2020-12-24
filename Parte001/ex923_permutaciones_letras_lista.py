# Ejercicio 923: Usar la función permutations() para generar las permutaciones de una lista de letras.

from itertools import permutations

letras = ['A', 'B', 'C', 'D', 'E']
print(letras)

print()

permutaciones = permutations(letras, 3)

contador = 0

for p in permutaciones:
    print(p)
    contador += 1

print()

print(f'Cantidad de permutaciones generadas: {contador}.')

print()

permutaciones = permutations(letras, 5)

contador = 0

for p in permutaciones:
    print(p)
    contador += 1

print()

print(f'Cantidad de permutaciones generadas: {contador}.')
