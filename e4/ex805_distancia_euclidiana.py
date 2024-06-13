# Ejercicio 805: Calcular la distancia euclidiana entre dos puntos en un espacio tridimensional.

from math import sqrt

def distancia_euclidiana_3d(punto_1, punto_2):
    distancia = sqrt(sum([(a - b) ** 2 for a, b in zip(punto_1, punto_2)]))

    return distancia

punto_1 = (2, 3, 5)
punto_2 = (7, 3, 11)

resultado = distancia_euclidiana_3d(punto_1, punto_2)

# (2 - 7) ** 2 + (3 - 3) ** 2 + (5 - 11) ** 2
# 25 + 0 + 36 = 61
# sqrt(61) = 

print(resultado)
