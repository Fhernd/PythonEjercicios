# Ejercicio 668: Obtener el número del día del año en curso.

import datetime

hoy = datetime.datetime.now()

numero_dia = (hoy - datetime.datetime(hoy.year, 1, 1)).days + 1

print('Número día del año:', numero_dia)
