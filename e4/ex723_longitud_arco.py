# Ejercicio 723: Crear una función para calcular la longitud de arco de un ángulo.

from math import pi

def longitud_arco(radio, angulo):
    resultado = 2 * pi * radio * (angulo/360)

    return resultado


print(longitud_arco(10, 45))
