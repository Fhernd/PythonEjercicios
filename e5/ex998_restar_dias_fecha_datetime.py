# Ejercicio 998: Restar una cantidad específica de días a un objeto de tipo datetime con timedelta.

from datetime import datetime, timedelta

fecha_hora_actual = datetime.now()
print(fecha_hora_actual)

print()

dias = 200
otra_fecha_hora = fecha_hora_actual - timedelta(dias, 0)
print(otra_fecha_hora)
