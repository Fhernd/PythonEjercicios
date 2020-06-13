# Ejercicio 822: Listar todos los archivos de texto plano que hay en un directorio.

from glob import glob

def listar_archivos_texto_plano(ruta):
    listado_archivos = glob(ruta)

    return listado_archivos


directorio = 'Parte001/*.txt'

resultado = listar_archivos_texto_plano(directorio)

for f in resultado:
    print(f)
