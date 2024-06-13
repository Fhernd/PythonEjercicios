# Ejercicio 995: Agregar una cantidad de segundos específica a un objeto de tipo datetime.

from datetime import datetime, timedelta

fecha_hora_actual = datetime.now()

print(fecha_hora_actual)

print()

nueva_fecha_hora = fecha_hora_actual + timedelta(0, 30)
print(nueva_fecha_hora)
