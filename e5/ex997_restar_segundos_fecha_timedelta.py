# Ejercicio 997: Restar una cantidad de segundos específica a una fecha con un objeto timedelta.

from datetime import datetime, timedelta

fecha_hora_actual = datetime.now()
print(fecha_hora_actual)

print()

otra_fecha_hora = fecha_hora_actual - timedelta(0, 30)
print(otra_fecha_hora)
