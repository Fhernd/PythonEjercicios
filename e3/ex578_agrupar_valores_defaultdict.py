# Ejercicio 578: Agrupar valores de un conjunto de tuplas usando la clase defaultdict.

from collections import defaultdict

lenguajes = (('Python', '2'), ('Python', '3'), ('Java', '6'), ('Java', '7'), ('Java', '8'), ('C#', '5'), ('C#', '6'), ('C#', '7'))

agrupacion = defaultdict(list)

for l, v in lenguajes:
    agrupacion[l].append(v)

print(agrupacion)
