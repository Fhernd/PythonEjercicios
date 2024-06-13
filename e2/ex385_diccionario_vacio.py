# Ejercicio 385: Comprobar si un objeto diccionario se encuentra vacío. 

d = {}

print(len(d) == 0)

print(not bool(d))

print(not d)

print()

d.update({1: 2})

print(len(d))

print(len(d) == 0)

print(not bool(d))

print(not d)
