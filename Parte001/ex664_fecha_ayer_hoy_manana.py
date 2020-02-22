# Ejercicio 664: Obtener la fecha de ayer, hoy y mañana con un objeto timedelta.

import datetime

hoy = datetime.date.today()
ayer = hoy - datetime.timedelta(1)
manana = hoy + datetime.timedelta(1)

print('Ayer:', ayer)
print('Hoy:', hoy)
print('Mañana:', manana)
