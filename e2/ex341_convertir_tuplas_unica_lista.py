# Ejercicio 341: Convertir un listado de tuplas a una única lista ordenada.

puntos = [(1, 2), (3, 4), (6, 7), (5, 4), (13, 11), (-1, -2), (0, 0), (5, 19)]
print(puntos)

conjunto = set().union(*puntos)
print(conjunto)

resultado = sorted(conjunto)
print(resultado)
