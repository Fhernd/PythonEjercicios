# Ejercicio 600: Uso de la clase Queue para crear una estructura de datos tipo cola.

from queue import Queue

clientes = Queue()
clientes.put('Edward')
clientes.put('Daniela')
clientes.put('Oliva')
clientes.put('Juan')

print(clientes.qsize())

print()

for c in list(clientes.queue):
    print(c, end=' ')
