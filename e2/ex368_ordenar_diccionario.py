# Ejercicio 368: Ordenar un diccionario de forma ascendente y descendente por valor.

from operator import itemgetter

d = {1: 5, 2: 8, 3: 2, 4: 7, 7: 0, 8: -1, 6: 5}

d_asc = dict(sorted(d.items(), key=itemgetter(1)))

print(d)
print(d_asc)

print()

d_desc = dict(sorted(d.items(), key=itemgetter(1), reverse=True))

print(d_desc)
