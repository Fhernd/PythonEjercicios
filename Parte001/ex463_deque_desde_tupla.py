# Ejercicio 463: Crear un objeto deque utilizando un objeto tupla.

from collections import deque

numeros = (5, 7, 11, 13)

print(type(numeros))
print(numeros)

print()

primos = deque(numeros)
print(type(primos))
print(primos)

print()

primos.appendleft(3)
primos.append(17)
print(primos)
