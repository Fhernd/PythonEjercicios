# Ejercicio 580: Crear una enumeración para representar colores básicos.

from enum import Enum

class Color(Enum):
    Negro = 1
    Blanco = 2
    Rojo = 3
    Verde = 4
    Azul = 5


print(Color.Negro)
print(Color.Blanco)
