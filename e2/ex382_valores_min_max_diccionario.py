# Ejercicio 382: Obtener el valor mínimo y máximo de un objeto diccionario.

productos = {'Mouse': 29, 'Teclado': 57.9, 'Monitor': 299, 'Audífonos': 25.9}

print(productos)

llave_minimo = min(productos.keys(), key=lambda k: productos[k])

print(llave_minimo, productos[llave_minimo])

llave_maximo = max(productos.keys(), key=lambda k: productos[k])

print(llave_maximo, productos[llave_maximo])
