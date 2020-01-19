# Ejercicio 591: Uso básico de la estructura de datos incorporada heapq.

import heapq

cola = []
heapq.heappush(cola, ('Python', '3.8.1'))
heapq.heappush(cola, ('Python', '2.7.1'))
heapq.heappush(cola, ('Java', '12'))

for e in cola:
    print(e)
