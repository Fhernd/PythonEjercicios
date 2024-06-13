# Ejercicio 601: Comprobar si una cola está vacía a través del método de instancia empty().

from queue import Queue

q = Queue()
print(q.empty())

print()

for i in range(5):
    q.put(i)

print(q.empty())
