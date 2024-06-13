# Ejercicio 999: Ordenar una lista de cadenas de caracteres según su longitud con la función sorted().

lenguajes = ['C#', 'Java', 'JavaScript', 'Python', 'PHP', 'Go', 'Kotlin']
print(lenguajes)

print()

# A-Z
lenguajes_ordenados = sorted(lenguajes)
print(lenguajes_ordenados)

print()

# Menor a mayor longitud (ascendente):
lenguajes_ordenados = sorted(lenguajes, key=len)
print(lenguajes_ordenados)

print()

# Mayor a menor longitud (descendente):
lenguajes_ordenados = sorted(lenguajes, key=len, reverse=True)
print(lenguajes_ordenados)
