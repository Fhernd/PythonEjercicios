# Ejercicio 745: Crear una función para calcular el área de un polígono regular.

from math import pi, tan

def area_poligono_regular(n, l):
    area = n * l**2 / (4 * tan(pi/n))

    return area


if __name__ == "__main__":
    n = 6
    l = 10
    resultado = area_poligono_regular(n, l)
    print(resultado)
