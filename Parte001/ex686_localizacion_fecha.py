# Ejercicio 686: Generar la fecha UTC (Universal Time Coordinated) con timezone.utc.

from datetime import datetime, timezone

fecha_utc = datetime.now(timezone.utc)

print(fecha_utc.strftime('%Y-%m-%d %H:%M:%S%z'))
