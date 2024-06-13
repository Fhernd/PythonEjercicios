# Ejercicio 744: Calcular la distancia entre dos puntos definidos por la latitud y la longitud.

from math import acos, cos, sin, radians

def distancia_puntos(punto_1, punto_2):
    punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
    punto_2 = (radians(punto_2[0]), radians(punto_2[1]))

    distancia = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1] - punto_2[1]))

    return distancia * 6371.01


if __name__ == "__main__":
    punto_1 = (4.6097100, -74.0817500)
    punto_2 = (55.7522202, 37.6155586)

    resultado = distancia_puntos(punto_1, punto_2)

    print('La distancia en kilómetros entre Bogotá y Moscú es de %f' % resultado)
