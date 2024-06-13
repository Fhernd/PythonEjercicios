# Ejercicio 929: Encadenar objetos iterables (colecciones) con la función chain().

from itertools import chain

cadena = 'Python'
numeros = [1, 2, 3, 4, 5, 6]

print(cadena)
print(numeros)

print()

resultado = list(chain(cadena, numeros))
print(resultado)

print()

reales = (3.1415, 2.7172, 1.4142)

resultado = list(chain(cadena, numeros, reales))
print(resultado)
