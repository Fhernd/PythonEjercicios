# Ejercicio 469: Rotación negativa de un objeto deque con el método de instancia rotate().

# [1, 2, 3, 4, 5], -2
# [3, 4, 5, 1, 2]

from collections import deque

numeros = deque([1, 2, 3, 4, 5])

print(numeros)

numeros.rotate(-2)

print(numeros)

numeros.rotate(-5)

print(numeros)
