# Ejercicio 349: Crear un contador infinito con la función count() de itertools.

from itertools import count

contador = count()

print(type(contador))

while True:
    print(next(contador))
