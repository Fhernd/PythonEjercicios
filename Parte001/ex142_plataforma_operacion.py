# Ejercicio 142: Obtener los datos básicos de la plataforma operacional.

import os, platform

print('Nombre de la plataforma: %s' % os.name)
print('Nombre del sistema operativo: %s' % platform.system())
print('Versión: %s' % platform.release())
