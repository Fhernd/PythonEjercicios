# Ejercicio 192: Calcular la media armónica y la media geométrica usando el módulo statistics.

from statistics import geometric_mean, harmonic_mean

media_g = geometric_mean([54, 24, 36])

print(round(media_g, 1))

media_a = harmonic_mean([40, 60])

print(media_a)
