# Ejercicio 920: Agrupar datos numéricos con la función groupby() del módulo incorporado itertools.

from itertools import groupby

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 9]
print(numeros)

print()

grupos_numeros = groupby(numeros)

for k, g in grupos_numeros:
    print(f'Llave: {k}')
    print(f'Grupo: {list(g)}')
    print()
