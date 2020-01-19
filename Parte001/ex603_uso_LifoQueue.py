# Ejercicio 603: Usar la clase LifoQueue para crear una estructura LIFO (Last-In-First-Out).

from queue import LifoQueue

pila = LifoQueue()

for i in range(1, 6):
    pila.put(i)

print(pila.qsize())

print()

while not pila.empty():
    print(pila.get())
