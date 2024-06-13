# Ejercicio 751: Computar la longitud y el ángulo de un número complejo.

import cmath

complejo = complex(2, 3)

print('Longitud: {}'.format(abs(complejo)))
print('Ángulo: {}'.format(cmath.phase(complejo)))
