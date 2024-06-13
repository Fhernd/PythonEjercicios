# Ejercicio 346: Ordenar una lista de diccionarios anidados por medio de su valor.

productos = [{'producto': {'valor': 1000}}, {'producto': {'valor': 3000}}, {'producto': {'valor': 2000}}]

print(productos)

print()

productos.sort(key=lambda p: p['producto']['valor'], reverse=True)

print(productos)
