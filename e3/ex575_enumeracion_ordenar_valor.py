# Ejercicio 575: Ordenar los nombres de una enumeración a partir de su valor.

from enum import IntEnum

class PuntoCardinal(IntEnum):
    Norte = 1
    Sur = 3
    Oeste = 4
    Este = 2


resultado = sorted(PuntoCardinal)
print(resultado)

resultado = '\n'.join(p.name for p in resultado)
print(resultado)
