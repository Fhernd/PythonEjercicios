# Ejercicio 106: Separar la ruta de la extensión de archivo.

import os.path

rutas = [r'C:\AUTOEXEC.BAT', '/etc/passwd', 'lenguajes.txt', '', 'code', r'C:\\', '/']

for ruta in rutas:
    print('%s: ' % ruta, os.path.splitext(ruta))
