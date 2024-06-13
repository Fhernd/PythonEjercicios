# Ejercicio 674: Remover los microsegundos de un objeto datetime usando replace().

import datetime

hoy = datetime.datetime.today()
print('Fecha actual:', hoy)

hoy = hoy.replace(microsecond=0)
print('Fecha actual (sin microsegundos):', hoy)
