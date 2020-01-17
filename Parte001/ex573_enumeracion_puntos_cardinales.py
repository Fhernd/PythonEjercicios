# Ejercicio 573: Crear una enumeración para representar los 4 puntos cardinales.

from enum import Enum

class PuntoCardinal(Enum):
    Norte = 1
    Sur = 2
    Este = 3
    Oeste = 4


print(PuntoCardinal.Norte.name)
print(PuntoCardinal.Norte.value)

print()

print(PuntoCardinal.Oeste.name)
print(PuntoCardinal.Oeste.value)
