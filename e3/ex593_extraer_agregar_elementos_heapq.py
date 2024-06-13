# Ejercicio 593: Extraer y agregar elementos a una estructura de datos heapq.

import heapq

cola = []
heapq.heappush(cola, ('Python', '3.8.1'))
heapq.heappush(cola, ('Python', '2.7.1'))
heapq.heappush(cola, ('Java', '12'))

for e in cola:
    print(e)

print()

heapq.heappushpop(cola, ('PHP', '7.1.2'))

for e in cola:
    print(e)
