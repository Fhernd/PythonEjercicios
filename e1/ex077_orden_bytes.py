# Ejercicio 77: Determinar el orden de los bytes en la arquitectura de ejecución actual.

# Big-Endian, Little-Endian

import sys

if sys.byteorder == 'little':
    print('Plataforma little-endian')
else:
    print('Plataforma big-endian')
