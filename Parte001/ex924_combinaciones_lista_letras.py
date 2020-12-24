# Ejercicio 924: Usar la función combinations() para generar las combinaciones de una lista de letras.

from itertools import combinations

letras = ['P', 'y', 't', 'h', 'o', 'n']
print(letras)

print()

resultado = combinations(letras, 1)

for c in resultado:
    print(c)

print()

resultado = combinations(letras, 2)

for c in resultado:
    print(c)

print()

resultado = combinations('Python', 2)

for c in resultado:
    print(c)
