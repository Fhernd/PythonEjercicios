# Ejercicio 683: Sumar seis (6) meses a una fecha específica usando timedelta.

from datetime import date, timedelta

fecha_actual = date.today()
seis_meses_despues = fecha_actual + timedelta(365/2)

print('Fecha actual:', fecha_actual)
print('Seis meses después:', seis_meses_despues)
