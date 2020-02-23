# Ejercicio 670: Obtener el número de la semana actual del año en curso.

import datetime

fecha_actual = datetime.date.today()
print('Fecha actual:', fecha_actual)

numero_semana = fecha_actual.isocalendar()

print('Número de la semana del año en curso:', numero_semana[1])
