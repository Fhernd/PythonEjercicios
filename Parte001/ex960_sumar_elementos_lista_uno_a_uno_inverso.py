# Ejercicio 960: Usar la función zip_longest() para sumar los elementos de dos listas índice a índice en sentido inverso.

from itertools import zip_longest

primos = [2, 3, 5, 7]
impares = [1, 3, 5, 7, 9, 11]

print('Contenido de la lista primos:', primos)
print('Cantidad de elementos de la lista primos:', len(primos))

print()

print('Contenido de la lista impares:', impares)
print('Cantidad de elementos de la lista impares:', len(impares))

print()

resultado = [x + y for x, y in zip_longest(reversed(impares), reversed(primos), fillvalue=0)]
print(resultado)
print(resultado[::-1])
