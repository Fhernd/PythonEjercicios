# Ejercicio 576: Obtener todos los valores declarados en una enumeración.

from enum import IntEnum

class PuntoCardinal(IntEnum):
    Norte = 1
    Sur = 3
    Oeste = 4
    Este = 2


valores = list(map(int, PuntoCardinal))
print(valores)
