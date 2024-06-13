# Ejercicio 465: Eliminar todos los elementos de un objeto deque con el método clear().

from collections import deque

d = deque([3, 5, 7])

print(len(d))
print(d)

print()

d.appendleft(2)
d.append(11)

print(len(d))
print(d)

print()

d.clear()

print(len(d))
print(d)
