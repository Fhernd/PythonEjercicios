# Ejercicio 572: Crear una función lambda para obtener las palabras con longitud mayor a 5.

lenguajes = ['Python', 'PHP', 'C', 'C++', 'Java', 'JavaScript', 'C#']
print(lenguajes)

print()

resultado = filter(lambda l: len(l) > 5, lenguajes)

for e in resultado:
    print(e)
