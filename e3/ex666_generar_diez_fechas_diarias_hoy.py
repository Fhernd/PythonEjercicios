# Ejercicio 666: Generar diez fechas a partir de la fecha actual.

import datetime

hoy = datetime.datetime.today()

print('Fecha actual:', hoy)

fechas = [hoy + datetime.timedelta(dia) for dia in range(1, 11)]

for f in fechas:
    print(f)
