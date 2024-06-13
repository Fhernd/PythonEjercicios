# Ejercicio 126: Encontrar el módulo al que pertenece un elemento de programa.

from inspect import getmodule

from math import sin

print(getmodule(sin))
print(type(getmodule(sin)))
print(dir(type(getmodule(sin))))
