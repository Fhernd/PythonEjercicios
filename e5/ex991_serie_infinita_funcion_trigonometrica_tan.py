# Ejercicio 991: Calcular la tangente de un ángulo usando las series infinitas del seno y el coseno.

import math

x = math.pi / 4

seno = 0

for n in range(0, 50):
    seno += math.pow(-1, n) / math.factorial(2 * n + 1) * math.pow(x, 2*n + 1)

coseno = 0

for k in range(0, 50):
    coseno += math.pow(-1, k)*math.pow(x, 2 * k) / math.factorial(2*k)

tangente = seno / coseno

print('El coseno calculado a partir de las series infinitas del seno y el coseno:', tangente)
print('El coseno calculado a partir de la función math.tan():', math.tan(x))
