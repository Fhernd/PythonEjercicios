# Ejercicio 389: Encontrar las llaves con los tres valores más grandes en un diccionario.

from heapq import nlargest

productos = {'Monitor': 299, 'Mouse': 27, 'Teclado': 73.9, 'Audífonos': 25.9, 'Smartphone': 450}

productos_mas_costosos = nlargest(3, productos, key=productos.get)

print(productos_mas_costosos)
