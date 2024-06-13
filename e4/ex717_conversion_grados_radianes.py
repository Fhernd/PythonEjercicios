# Ejercicio 717: Crear una función para convertir grados a radianes.

from math import pi

def grados_radianes(grados):
    """
    Convierte una cantidad de grados en radianes.
    """
    radianes = grados * (pi / 180)

    return radianes

print(grados_radianes(180)) # 3.1415...
print(grados_radianes(90)) # 1.5708
