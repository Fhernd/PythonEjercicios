# Ejercicio 64: Consultar la fecha de creación y modificación de un archivo.

import os.path, time

nombre_archivo = 'archivo.txt'

print('Fecha creación: {}'.format(time.ctime(os.path.getctime(nombre_archivo))))
print('Fecha modificación: {}'.format(time.ctime(os.path.getmtime(nombre_archivo))))
