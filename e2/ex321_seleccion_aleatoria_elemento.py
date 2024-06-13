# Ejercicio 321: Seleccionar de forma aleatoria un elemento de una lista con random.choice().

from random import choice

lenguajes = ['Python', 'Java', 'C++', 'JavaScript', 'C', 'PHP', 'C#']

print(lenguajes)

lenguaje_aleatorio = choice(lenguajes)

print(lenguaje_aleatorio)

print()

for _ in range(10):
    print(choice(lenguajes))
