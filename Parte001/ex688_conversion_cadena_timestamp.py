# Ejercicio 688: Convertir una cadena de caracteres de una fecha a una marca de tiempo (timestamp).

import datetime
import time

fecha_cadena = '1972/06/23'

resultado = time.mktime(datetime.datetime.strptime(fecha_cadena, '%Y/%m/%d').timetuple())

print(resultado)
