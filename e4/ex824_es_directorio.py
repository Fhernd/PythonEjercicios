# Ejercicio 824: Comnprobar si una ruta corresponde con un directorio (carpeta).

import os

ruta = 'Parte001/ciudades.txt'

print(os.path.isdir(ruta))

print()

ruta = 'Parte001/'

print(os.path.isdir(ruta))
