# Ejercicio 595: Obtener el mínimo y el máximo de una lista con usando el módulo heapq.

import heapq

primos = [19, 11, 29, 3, 7, 37, 2, 5]

print('Mínimo:', heapq.nsmallest(1, primos))
print('Máximo:', heapq.nlargest(1, primos))
