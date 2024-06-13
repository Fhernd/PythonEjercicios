# Ejercicio 461: Acceder a un elemento de un objeto Counter.

from collections import Counter

c = Counter(rojo=255, verde=0, azul=0)

print(c)

print(c['rojo'])
print(c['verde'])
print(c['azul'])

print()

print(c['amarillo'])
