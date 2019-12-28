# Ejercicio 439: Orden descendente una lista de tuplas por el valor de punto flotante de cada tupla.

productos = [('Mouse', '29.5'), ('Teclado', '77.9'), ('Auriculares', '15.9'), ('Deademas', '49.9')]

print(productos)

resultado = sorted(productos, key=lambda p: float(p[1]), reverse=True)

print(resultado)
