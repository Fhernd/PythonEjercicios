# Ejercicio 574: Iterar todos los elementos que contiene una enumeración en un ciclo for.

from enum import Enum

class PuntoCardinal(Enum):
    Norte = 1
    Sur = 2
    Este = 3
    Oeste = 4


for p in PuntoCardinal:
    print('{:10}: {}'.format(p.name, p.value))
