# Ejercicio 605: Uso de la clase SimpleQueue del módulo incorporado queue.

from queue import SimpleQueue

q = SimpleQueue()

for i in range(1, 6):
    q.put(i)

print(q.qsize())

print()

while not q.empty():
    print(q.get())
