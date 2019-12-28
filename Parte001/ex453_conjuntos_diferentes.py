# Ejercicio 453: Comprobar si dos conjuntos no tienen elementos en común con isdisjoint().

colores_1 = set(['Negro', 'Blanco'])
colores_2 = set(['Azul', 'Rojo', 'Negro'])
colores_3 = set(['Gris'])

print(colores_1)
print(colores_2)
print(colores_3)

print()

print(colores_1.isdisjoint(colores_2))

print()

print(colores_1.isdisjoint(colores_3))

print()

print(colores_2.isdisjoint(colores_3))
