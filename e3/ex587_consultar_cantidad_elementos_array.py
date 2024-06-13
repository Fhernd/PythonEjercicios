# Ejercicio 587: Usar len() para consultar la cantidad de elementos de un objeto array.

from array import array

enteros = array('i', [2, 3, 5, 7, 11, 13, 17])
print(len(enteros))

enteros.append(19)
enteros.append(23)

print(len(enteros))
