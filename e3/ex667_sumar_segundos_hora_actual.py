# Ejercicio 667: Sumar 5 segundos a la hora actual por medio de timedelta.

import datetime

hora_actual = datetime.datetime.now()
print('Hora actual:', hora_actual)

resultado = hora_actual + datetime.timedelta(seconds=5)

print('Hora más 5 segundos:', resultado)
