# Ejercicio 71: Calcular el tamaño de un archivo.

import os

archivo = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\ex071_archivo_tamagnio.py'


def calcular_tamagnio_archivo(archivo):
    """
    Calcula el tamaño de un archivo.
    """
    try:
        return os.path.getsize(archivo)
    except:
        return None


print(calcular_tamagnio_archivo(archivo))

archivo = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\ex071_archivo_tamagnio.ph'

print(calcular_tamagnio_archivo(archivo))
