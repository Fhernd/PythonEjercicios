# Ejercicio 662: Substraer 10 días a la fecha actual usando un objeto timedelta.

from datetime import date, timedelta

fecha_actual = date.today()
resultado = fecha_actual - timedelta(10)

print('Fecha actual:', fecha_actual)
print('10 días antes de la fecha actual:', resultado)
