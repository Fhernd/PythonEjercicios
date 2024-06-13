# Ejercicio 795: Usar una cadena de formato para un objeto fecha.

from datetime import datetime

fecha = datetime(2012, 10, 8, 7, 13, 43)

print(fecha)

print()

print('{:%Y/%m/%d %H:%M}'.format(fecha))
