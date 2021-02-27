# Ejercicio 981: Calcular el producto cartesiano usando una lista de comprensión.

def producto_cartesiano(datos):

    return [(d, e) for d in datos[0] for e in datos[1]]

datos = [[1, 2], [3, 4]]

print(producto_cartesiano(datos)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

print()

datos = [[1, 2, 3], [4, 5, 6]]
print(producto_cartesiano(datos)) # [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
