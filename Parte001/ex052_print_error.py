# Ejercicio 52: Imprimir en la salida estándar de errores.

import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr)


eprint('Este es un mensaje de error')
