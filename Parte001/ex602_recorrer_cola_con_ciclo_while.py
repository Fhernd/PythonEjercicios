# Ejercicio 602: Recorrer todos los elementos de una cola por medio de un ciclo while.

from queue import Queue

q = Queue()

for i in range(5):
    q.put(i)

print(q.qsize())

print()

while not q.empty():
    print(q.get(), end=' ')
