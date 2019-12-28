# Ejercicio 462: Manipular un objeto deque con sus operaciones básicas.

from collections import deque

colores = deque(['Rojo', 'Verde', 'Azul'])

print(len(colores))
print(colores)

print()

colores.appendleft('Negro')
print(len(colores))
print(colores)

print()

colores.append('Blanco')
print(len(colores))
print(colores)

print()

colores.popleft()
print(len(colores))
print(colores)

print()

colores.pop()
print(len(colores))
print(colores)

print()

colores.reverse()
print(colores)
