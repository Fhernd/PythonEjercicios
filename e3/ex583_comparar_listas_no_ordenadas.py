# Ejercicio 583: Comparar si dos listas no ordenadas contienen los mismos elementos.

from collections import Counter

def comparar_listas(a, b):
    return Counter(a) == Counter(b)

numeros_1 = [7, 5, 3, 2, 1, 11, 3, 2]
numeros_2 = [7, 13, 3, 2, 1, 11, 3, 2]
numeros_3 = [7, 5, 3, 2, 1, 11, 3, 2]

print(comparar_listas(numeros_1, numeros_2))
print(comparar_listas(numeros_2, numeros_3))
print(comparar_listas(numeros_1, numeros_3))
