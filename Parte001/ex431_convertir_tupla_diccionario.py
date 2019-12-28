# Ejercicio 431: Convertir un objeto tupla en un objeto diccionario.

lenguajes = (('Python', '3.8.1'), ('JavaScript', 'ES6'), ('C#', '7.0'), ('PHP', '7.1.2'))

print(lenguajes)

lenguajes_diccionario = dict((l, v) for l, v in lenguajes)

print()

print(type(lenguajes_diccionario))
print(lenguajes_diccionario)
