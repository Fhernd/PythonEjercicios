# Ejercicio 961: Obtener todas las combinaciones de los tres colores primarios con el módulo itertools.

from itertools import combinations

colores = ['rojo', 'verde', 'azul']

print('El contenido de la variable colores es:', colores)

print()

combinaciones = []

for i in range(len(colores) + 1):
    combinaciones.append(list(combinations(colores, i)))

for c in combinaciones:
    print(c)
