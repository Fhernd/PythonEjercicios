# Ejercicio 585: Consultar el tamaño en bytes de los elementos de un objeto array.

from array import array

enteros = array('i', [2, 3, 5])
print(enteros.itemsize)

print()

reales = array('d', [3.1415, 2.7172])
print(reales.itemsize)
