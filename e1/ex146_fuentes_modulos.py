# 146: Encontrar las rutas en disco donde se hallan las fuentes de los módulos Python.

import sys, os

print('Lista de directorios del módulo `sys`:')
print('\n'.join(sys.path))

print()

print('Lista de directorios del módulo `os`:')
print(os.path)
