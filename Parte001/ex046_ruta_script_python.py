# Ejercicio 46: Encontrar la ruta del script actual en ejecución.

import os

print(os.path.realpath(__file__))
