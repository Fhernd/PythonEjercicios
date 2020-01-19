# Ejercicio 592: Extraer elementos de un objeto heapq con el método heappop().

import heapq

cola = []
heapq.heappush(cola, ('Python', '3.8.1'))
heapq.heappush(cola, ('Python', '2.7.1'))
heapq.heappush(cola, ('Java', '12'))

print(cola[0])

elemento = heapq.heappop(cola)
print(elemento)

print()

for e in cola:
    print(e)
