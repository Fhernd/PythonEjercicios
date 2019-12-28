# Ejercicio 450: Comprobar si un conjunto es subconjunto o superconjunto de otro conjunto.

colores_1 = set(['Negro', 'Blanco'])
colores_2 = set(['Blanco', 'Rojo'])
colores_3 = set(['Blanco'])

print(colores_1)
print(colores_2)
print(colores_3)

print()

subconjunto = colores_1 <= colores_2
print(subconjunto)

print()

superconjunto = colores_1 >= colores_2
print(superconjunto)

print()

subconjunto = colores_3 <= colores_2
print(subconjunto)

print()

superconjunto = colores_2 >= colores_3
print(superconjunto)
