# Ejercicio 761: Realizar operaciones aritméticas básicas con fracciones.

from fractions import Fraction

un_medio = Fraction(1, 2)
un_tercio = Fraction(1, 3)

print('{} + {} = {}'.format(un_medio, un_tercio, un_medio + un_tercio))
print('{} - {} = {}'.format(un_medio, un_tercio, un_medio - un_tercio))
print('{} * {} = {}'.format(un_medio, un_tercio, un_medio * un_tercio))
print('{} / {} = {}'.format(un_medio, un_tercio, un_medio / un_tercio))
