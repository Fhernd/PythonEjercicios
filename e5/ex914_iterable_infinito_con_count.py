# Ejercicio 914: Utilizar la función count() de itertools para generar un contador infinito.

from itertools import count
from time import sleep

inicio = 100
salto = 200

contador = count(inicio, salto)

for c in contador:
    print(c)

    if c > 100000:
        break

print('El contador ha finalizado.')

print()

contador = count(inicio, salto)

for c in contador:
    print(c)

    sleep(1)
