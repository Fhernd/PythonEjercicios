# Ejercicio 915: Generar un ciclo infinito entre los elementos de un elemento iterable (lista o tupla).

# ['Python', 'C#', 'JavaScript', 'Java']

from itertools import cycle
from time import sleep

ciclo_lenguajes = cycle(['Python', 'C#', 'JavaScript', 'Java'])

for c in ciclo_lenguajes:
    print(c)

    sleep(1)
