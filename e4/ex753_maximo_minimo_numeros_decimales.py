# Ejercicio 753: Encontrar el mínimo y el máximo de un conjunto de números decimales.

from decimal import Decimal

cadena = '2.54 2.73 2.71 3.14 2.00 0.04 1.19'
lista = cadena.split()
decimales = list(map(Decimal, lista))

print(decimales)

minimo = min(decimales)
maximo = max(decimales)

print(minimo)
print(maximo)
