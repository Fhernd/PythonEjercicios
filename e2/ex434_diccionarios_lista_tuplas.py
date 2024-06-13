# Ejercicio 434: Crear un objeto diccionario a partir de una lista de objetos tupla.

lista_tuplas = [('a', 1), ('b', 2), ('a', 2), ('b', 3), ('c', 1), ('e', 5), ('c', 2), ('b', 1), ('b', 5)]

d = {}

for x, y in lista_tuplas:
    d.setdefault(x, []).append(y)

print(d)
