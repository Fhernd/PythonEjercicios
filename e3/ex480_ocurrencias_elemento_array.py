# Ejercicio 480: Contar el numero de ocurrencias de un elemento en un objeto array.

from array import array

numeros = array('i', [2, 3, 2, 2, 5, 7, 7, 7, 13, 7, 7, 11, 2, 5, 19, 23, 29])

print(len(numeros))
print(numeros)

print()

conteo_7 = numeros.count(7)

print(conteo_7)
