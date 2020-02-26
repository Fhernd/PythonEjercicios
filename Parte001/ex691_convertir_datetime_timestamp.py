# Ejercicio 691: Convertir un objeto fecha (datetime) a una marca de tiempo (timestamp).

import datetime
import time

fecha = datetime.datetime(2013, 12, 27)
print(type(fecha))
print('Fecha y hora:', fecha)

marca_tiempo = time.mktime(fecha.timetuple())
print('Marca de tiempo:', marca_tiempo)
