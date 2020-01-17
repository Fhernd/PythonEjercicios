# Ejercicio 559: Crear una función lambda para ordenar las tuplas contenidas en una lista.

productos = [('Mouse', 29.5), ('Audífonos', 19.9), ('Teclado', 59.0), ('Monitor', 259)]
print(productos)

print()

productos.sort(key=lambda p: p[1], reverse=True)
print(productos)
