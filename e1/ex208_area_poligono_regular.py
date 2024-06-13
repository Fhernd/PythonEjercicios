# Ejercicio 208: Calcular el área de un polígono regular dados sus lados y la longitud de cada lado.

from math import pi, tan

def area_poligono_regular(n, s):
    area = n * s**2 / (4 * tan(pi/n))

    return area


numero_lados = 5
longitud_lados =  12

print(area_poligono_regular(numero_lados, longitud_lados))
