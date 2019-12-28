# Ejercicio 387: Obtener los valores únicos de una lista de diccionarios.

productos = [{'id': 101}, {'id': 201}, {'id': 301}, {'id': 101}, {'id': 101}, {'id': 301}, {'id': 401}, {'id': 401}]

ids_unicos = set(idp for p in productos for idp in p.values())

print(ids_unicos)
