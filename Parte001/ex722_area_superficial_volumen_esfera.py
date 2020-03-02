# Ejercicio 722: Crear funciones para calcular el área superficial y el volumen de una esfera.

from math import pi

def area_supeficial(r):
    area = 4 * pi * r ** 2

    return area

def volumen(r):
    resultado = 4/3 * pi * r**3

    return resultado


radio = 5
print(area_supeficial(radio))
print(volumen(5))
