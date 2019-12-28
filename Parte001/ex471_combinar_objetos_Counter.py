# Ejercicio 471: Combinar dos objetos Counter con el operador sobrecargado +.

from collections import Counter

contador_1 = Counter([1, 2, 3, 4, 5])
contador_2 = Counter([1, 2, 3, 4, 5])

print(contador_1)
print(contador_2)

print()

contador_3 = contador_1 + contador_2

print(contador_3)
