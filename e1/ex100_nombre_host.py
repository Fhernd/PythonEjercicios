# Ejercicio 100: Obtener el nombre del host donde se ejecuta un script.

import socket

nombre_host = socket.gethostname()

print('El nombre del host es %s' % nombre_host)
