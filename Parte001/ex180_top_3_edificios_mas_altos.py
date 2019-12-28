# Ejercicio 180: Encontrar los tres edificios más altos de un conjunto de 10 edificios.

# Solución:

from random import randint, seed

seed(0)

alturas = [randint(50, 500) for i in range(10)]

print(alturas)

alturas = sorted(alturas)

print(alturas)

edificios_mas_altos = alturas[-3:]

print(edificios_mas_altos)
