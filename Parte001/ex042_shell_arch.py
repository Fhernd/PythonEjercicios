# Ejercicio 42: Encontrar la arquitectura computacional del shell.

import struct

print(struct.calcsize('P') * 8)
