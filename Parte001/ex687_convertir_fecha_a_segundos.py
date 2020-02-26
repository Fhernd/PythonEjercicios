# Ejercicio 687: Convertir un objeto fecha (datetime) a una marca de tiempo (timestamp).

import datetime
import time

def convertir_fecha_timestamp(fecha):
    fecha = fecha.timetuple()
    resultado = time.mktime(fecha)

    return resultado

ahora = datetime.datetime.now()
print(convertir_fecha_timestamp(ahora))
