# Ejercicio 466: Copiar los elementos de un objeto deque con el método de instancia copy().

from collections import deque

numeros = deque([2, 3, 5, 7, 11])

print(numeros)
print('ID:', id(numeros))

print()

numeros_copia = numeros.copy()

print(numeros_copia)
print('ID:', id(numeros_copia))
