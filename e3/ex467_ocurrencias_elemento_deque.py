# Ejercicio 467: Contar el número de ocurrencias de un elemento en un objeto deque.

from collections import deque

numeros = deque((3, 5, 7, 2, 2, 2, 3, 5, 7, 13, 11, 2, 3, 5))

print(len(numeros))
print(numeros)

print()

conteo_dos = numeros.count(2)
print('El valor 2 aparece {} veces.'.format(conteo_dos))
