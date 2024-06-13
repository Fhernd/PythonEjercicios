# Ejercicio 136: Excluir directorios durante la exploración de un directorio específico.

import os

ruta = r'C:\Windows'

archivos = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]

print(archivos)
