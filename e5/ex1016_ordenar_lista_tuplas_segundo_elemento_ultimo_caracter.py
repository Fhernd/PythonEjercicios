# Ejercicio 1016: Ordenar una lista de tuplas a partir del último carácter del segundo elemento de cada tupla.

datos = [(1003, 'Desktop Clone'), (1004, 'Gamer portátil'), (1002, 'Tablet'), (1003, 'Apple MacBook')]
print(datos)

print()

datos_ordenados = sorted(datos, key=lambda c: c[1][-1])
print(datos_ordenados)
