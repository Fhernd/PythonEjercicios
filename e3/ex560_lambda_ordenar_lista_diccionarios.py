# Ejercicio 560: Crear una función lambda para ordenar una lista de diccionarios.

productos = [{'nombre': 'Teclado', 'precio': 55.9, 'color': 'Negro'}, {'nombre': 'Mouse', 'precio': 25.9, 'color': 'Gris'}, {'nombre': 'Monitor', 'precio': 255.9, 'color': 'Negro'}, {'nombre': 'Audífonos', 'precio': 39.9, 'color': 'Blanco'}, {'nombre': 'Mac', 'precio': 755.9, 'color': 'Plateado'}]

print(productos)

print()

productos = sorted(productos, key=lambda p: p['color'])
print(productos)
