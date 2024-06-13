# Ejercicio 486: Eliminar la primera ocurrencia de un valor en un objeto array con remove().

from array import array

numeros = array('i', [2, 2, 3, 2, 5, 5, 3, 7, 7, 11, 13, 17, 19])

print(len(numeros))
print(numeros)

print()

numeros.remove(2)
print(len(numeros))
print(numeros)

print()

numeros.remove(3)
print(len(numeros))
print(numeros)
