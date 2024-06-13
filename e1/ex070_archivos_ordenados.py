# Ejercicio 70: Ordenar un conjunto de archivos por fecha de creación.

import glob
import os

ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001'

archivos = glob.glob(ruta + os.path.sep + '*.py')

archivos.sort(key=os.path.getctime)

print('\n'.join(archivos))
