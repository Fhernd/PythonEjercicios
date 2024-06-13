# Ejercicio 754: Sumar y ordenar un conjunto de números decimales.

from decimal import Decimal

cadena = '2.54 2.73 2.71 3.14 2.00 0.04 1.19'
lista = cadena.split()
print(lista)

decimales = list(map(Decimal, lista))
print(decimales)

suma = sum(decimales)
decimales = sorted(decimales)

print()

print('Suma: %f' % suma)
print(decimales)
