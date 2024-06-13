# Ejercicio 107: Obtener las propiedades básicas de un archivo.

import os
import time

archivo = 'archivo.txt'

print('Archivo: %s' % archivo)
print('Fecha modificación: {}'.format(time.ctime(os.path.getmtime(archivo))))
print('Fecha acceso: {}'.format(time.ctime(os.path.getatime(archivo))))
print('Fecha cambio: {}'.format(time.ctime(os.path.getctime(archivo))))
print('Tamaño: %d bytes' % os.path.getsize(archivo))
