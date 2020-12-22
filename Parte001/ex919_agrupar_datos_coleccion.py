# Ejercicio 919: Usar la función groupby() de itertools para agrupar datos de una colección.

from itertools import groupby

texto = 'AAAAABBCCCDDDEEEEEEEFFGHHHHHIIaaaa'
print(texto)

print()

grupos = groupby(texto)

for k, g in grupos:
    print(f'Llave: {k}')
    print(f'Grupo: {list(g)}')
    print()
