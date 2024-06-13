# Ejercicio 417: Desempaquetar los elementos de una tupla en diferentes variables.

punto_3d = (2, 3, 5)

print(punto_3d)
print(len(punto_3d))

x, y, z = punto_3d

print(x, y, z)

print()

punto_3d = (7, 11, 13)

x, _, z = punto_3d

print(x, z)
