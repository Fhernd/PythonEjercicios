# Ejercicio 63: Comprobar si el nombre de un archivo corresponde con una ruta absoluta.

from os import path

nombre_archivo_1 = 'archivo.txt'
nombre_archivo_2 = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001\archivo.txt'

print(path.isabs(nombre_archivo_1))
print(path.isabs(nombre_archivo_2))
print(__file__)
print(path.isabs(__file__))
