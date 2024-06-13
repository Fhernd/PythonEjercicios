# Ejercicio 49: Mostrar los archivos de un directorio específico.

from os import listdir
from os.path import isfile, join

ruta = r'D:\Dropbox\Pro\Ejercicios\PythonEjercicios\Parte001'


def listar_directorio(ruta):
    """
    Lista el contenido de archivos de un directorio específico.
    """
    archivos = [a for a in listdir(ruta) if isfile(join(ruta, a))]

    return archivos


listado_archivos = listar_directorio(ruta)

print(listado_archivos)
print(len(listado_archivos))
