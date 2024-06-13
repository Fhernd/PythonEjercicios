# Ejercicio 964: Recorrer los grupos de datos identificados con la función groupby() de itertools.
    
from itertools import groupby

letras = ['B', 'A', 'C', 'A', 'A', 'B', 'D', 'C', 'B', 'B', 'B', 'B']
print(letras)

letras.sort()
print(letras)

print()

grupos_letras = groupby(letras)
print(grupos_letras)

print()

for g, d in grupos_letras:
    datos = list(d)
    print(g, '-->', datos, f'({len(datos)})')
