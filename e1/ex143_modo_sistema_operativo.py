# Ejercicio 143: Detectar el modo del sistema operativo (32 ó 64 bits).

import struct

modo_so = struct.calcsize('P') * 8

print('El sistema operativo actual es de %i bits' % modo_so)
