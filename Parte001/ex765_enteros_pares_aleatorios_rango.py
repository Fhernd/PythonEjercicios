# Ejercicio 765: Generar varios números enteros pares aleatorios dentro de un rango específico.

import random

for _ in range(10):
    print(random.randrange(0, 100, 2), end=' ')
