# Ejercicio 724: Crear una función para calcular el área de un sector de un círculo.

from math import pi

def area_sector_circulo(radio, radianes):
    area = 1/2 * radio ** 2 * radianes

    return area

print(area_sector_circulo(5, pi/2))
