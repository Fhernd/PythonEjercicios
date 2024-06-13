# Ejercicio 111: Seleccionar archivos de un tipo específico.

import glob
import os

ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001'

comodin = '*.py'

lista_archivos = glob.glob(ruta + os.sep + comodin)

print(lista_archivos)
