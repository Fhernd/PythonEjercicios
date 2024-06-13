# Ejercicio 1000: Ordenar una lista de cadenas de caracteres según el último carácter con la función sorted().

lenguajes = ['C#', 'Java', 'JavaScript', 'Python', 'PHP', 'Go', 'Kotlin']
print(lenguajes)

print()

# Orden ascendente de la lista según último carácter:
lenguajes_ordenados = sorted(lenguajes, key=lambda l: l[-1])
print(lenguajes_ordenados)

print()

# Orden descendente de la lista según último carácter:
lenguajes_ordenados = sorted(lenguajes, key=lambda l: l[-1], reverse=True)
print(lenguajes_ordenados)
