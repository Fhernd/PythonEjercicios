# Ejercicio 108: Consultar propiedades de archivos y directorios.

import os

rutas = ['archivo.txt', r'C:\Windows', 'no_existe.txt', os.path.dirname(r'C:\Windows'), __file__]

for ruta in rutas:
    print('Archivo: %s' % ruta)
    print('¿Existe?: {}'.format(os.path.exists(ruta)))
    print('¿Es ruta absoluta?: {}'.format(os.path.isabs(ruta)))
    print('¿Es archivo?: {}'.format(os.path.isfile(ruta)))
    print('¿Es carpeta?: {}'.format(os.path.isdir(ruta)))
    print()
