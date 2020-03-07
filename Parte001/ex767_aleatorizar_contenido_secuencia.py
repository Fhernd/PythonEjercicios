# Ejercicio 767: Aleatorizar el contenido de una colección o secuencia con la función shuffle().

import random
from string import ascii_uppercase

numeros = [1, 2, 3, 4, 5]

print(numeros)

random.shuffle(numeros)

print(numeros)

print()

mayusculas = list(ascii_uppercase)

print(mayusculas)

random.shuffle(mayusculas)

print(mayusculas)
