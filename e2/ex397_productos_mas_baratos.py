# Ejercicio 397: Encontrar los 3 productos más baratos desde un objeto diccionario.

from heapq import nsmallest
from operator import itemgetter

productos = {'Mouse': 29.9, 'Memoria USB': 13.5, 'Monitor': 299.9, 'Deademas': 57.9, 'Teclado': 63.9}

print(productos)
print(len(productos))

for n, p in nsmallest(3, productos.items(), key=itemgetter(1)):
    print('{}: ${}'.format(n, p))
