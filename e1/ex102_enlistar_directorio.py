# Ejercicio 102: Mostrar el contenido de un directorio por medio de subprocess.

import subprocess

resultado = subprocess.check_output('dir', shell=True, universal_newlines=True)

print(resultado)
