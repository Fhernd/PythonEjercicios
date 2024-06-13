# Ejercicio 62: Obtener la ruta absoluta de un archivo.

from os import path

nombre_archivo = 'archivo.txt'

print(path.abspath(nombre_archivo))
