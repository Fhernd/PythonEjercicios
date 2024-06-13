# Ejercicio 85: Determinar si una ruta corresponde con un archivo o carpeta.

import os


def validar_ruta(ruta):
    if os.path.isdir(ruta):
        return 'Es un directorio'
    elif os.path.isfile(ruta):
        return 'Es un archivo'
    else:
        return 'Es un archivo especial (socket, dispositivo de gestión archivos)'


ruta = r'D:\Dropbox\Pro\Tutorship\Java'

print(validar_ruta(ruta))

ruta = r'D:\Dropbox\Pro\Tutorship\Java\Reloj.jpg'

print(validar_ruta(ruta))
