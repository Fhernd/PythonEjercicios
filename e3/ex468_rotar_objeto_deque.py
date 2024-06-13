# Ejercicio 468: Rotar un objeto deque una cantidad arbitraria de veces con el método rotate().

# [1, 2, 3], 1, 2
# [3, 1, 2]
# [2, 3, 1]

from collections import deque

numeros = deque([1, 2, 3, 4, 5])

print(numeros)

print()

numeros.rotate(3)

# 3, 4, 5, 1, 2

print(numeros)

print()

numeros.rotate(len(numeros))

print(numeros)
