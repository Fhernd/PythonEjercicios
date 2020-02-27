# Ejercicio 694: Crear función para obtener la última fecha de modificación de un archivo.

from datetime import datetime
import time
import os

def ultima_fecha_modificacion(ruta_archivo):
    estado = os.stat(ruta_archivo)
    fecha = time.localtime(estado.st_mtime)
    fecha = datetime(fecha[0], fecha[1], fecha[2], fecha[3], fecha[4], fecha[5])
    return fecha

nombre_archivo = 'Parte001/lenguajes.txt'
resultado = ultima_fecha_modificacion(nombre_archivo)
print(resultado)
