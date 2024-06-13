# Ejercicio 762: Obtener diferentes aproximaciones racionales de la constante pi.

from fractions import Fraction
from math import pi

print('Valor de pi:', pi)

fraccion_pi = Fraction(str(pi))

print('fraccion_pi:', fraccion_pi)

print()

denominadores = [1, 5, 50, 90, 100, 500, 1000, 10000, 1000000]

for d in denominadores:
    fraccion = fraccion_pi.limit_denominator(d)
    print(fraccion)
