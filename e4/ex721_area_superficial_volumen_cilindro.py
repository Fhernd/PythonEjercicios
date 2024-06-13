# Ejercicio 721: Crear funciones para calcular el área superficial y el volumen de un cilindro.

from math import pi

def volumen_cilindro(r, h):
    volumen = pi * r**2 * h

    return volumen

def area_superficial_cilindro(r, h):
    area = 2 * pi * r**2 + 2 * pi * r * h

    return area

radio = 5
altura = 7
print(f'Volumen del cilindro: {volumen_cilindro(radio, altura)}')
print(f'Área superficial del cilindro: {area_superficial_cilindro(radio, altura)}')
