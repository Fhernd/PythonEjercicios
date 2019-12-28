# Ejercicio 103: Obtener el nombre de archivo de una ruta absoluta.

import os

ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\ex030_mcd.py'

nombre_archivo = os.path.basename(ruta)

print(nombre_archivo)
