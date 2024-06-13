# Ejercicio 718: Crear una función para convertir radianes a grados.

import math

def radianes_a_grados(radianes):
    grados = radianes * (180 / math.pi)

    return grados

print(radianes_a_grados(math.pi)) # 180
print(radianes_a_grados(math.pi/2)) # 90
print(radianes_a_grados(math.pi/3)) # 60
