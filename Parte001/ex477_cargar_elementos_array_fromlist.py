# Ejercicio 477: Cargar elementos a un objeto array desde una lista con fromlist().

from array import array

numeros = array('i')

print(len(numeros))
print(numeros)

print()

primos = [2, 3, 5, 7, 11, 13, 17, 19]
numeros.fromlist(primos)
print(len(numeros))
print(numeros)
