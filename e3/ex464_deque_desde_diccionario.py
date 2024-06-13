# Ejercicio 464: Crear un objeto deque a partir de un objeto diccionario.

from collections import deque

d = {'a': 1, 'b': 2, 'c': 3}

letras = deque(d)

print(len(letras))
print(letras)

print()

letras.appendleft('f')
letras.append('d')

print(len(letras))
print(letras)

print()

letras.extend({'g': 8, 'h': 9})
print(len(letras))
print(letras)
