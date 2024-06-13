# Ejercicio 360: Iterar sobre dos listas de forma simultánea con la función zip().

nombres_colores = ['Blanco', 'Negro', 'Rojo', 'Verde', 'Azul']
codigos_colores = ['#FFFFFF', '#000000', '#FF0000', '#00FF00', '#0000FF']

print(nombres_colores)
print(codigos_colores)

print()

for n, c in zip(nombres_colores, codigos_colores):
    print(n, c)
