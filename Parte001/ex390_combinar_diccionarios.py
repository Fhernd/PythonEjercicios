# Ejercicio 390: Combinar los elementos de una lista de diccionarios con la clase Counter.

from collections import Counter

productos = [{'id': 1, 'precio': 1000}, {'id': 2, 'precio': 2000}, {'id': 1, 'precio': 1000}, {'id': 3, 'precio': 3000}, {'id': 3, 'precio': 3000}, {'id': 4, 'precio': 4000}, {'id': 3, 'precio': 3000}, {'id': 5, 'precio': 5000}, {'id': 1, 'precio': 1000}, {'id': 5, 'precio': 5000}]

resultado = Counter()

for p in productos:
    resultado[p['id']] += p['precio']

print(resultado)
