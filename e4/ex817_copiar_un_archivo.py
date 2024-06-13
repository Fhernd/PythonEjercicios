# Ejercicio 817: Copiar un archivo con la función copyfile() del módulo shutil.

from shutil import copyfile

archivo_origen = 'Parte001/lorem.txt'
archivo_destino = 'Parte001/lorem_copia.txt'

copyfile(archivo_origen, archivo_destino)
