# Ejercicio 127: Comprobar si un elemento de programa dado es una clase.

from inspect import isclass
from collections import Counter
from math import cos

print(isclass(Counter))
print(isclass(cos))


class Clase:
    pass


def funcion():
    pass


print()

print(isclass(Clase))
print(isclass(funcion))
