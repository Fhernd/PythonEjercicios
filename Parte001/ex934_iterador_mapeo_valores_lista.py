# Ejercicio 934: Crear un iterador para recorrer el resultado de aplicar una función sobre una colección de datos.

from itertools import starmap
from math import pow

datos = [(2, 3), (5, 2), (3, 9)]

resultado = list(starmap(pow, datos))

print(resultado)    # 8, 25, 19683
