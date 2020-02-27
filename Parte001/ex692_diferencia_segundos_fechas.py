# Ejercicio 692: Calcular diferencia en segundos entre dos objetos fecha.

from datetime import datetime, time

def diferencia_segundos_fechas(fecha_1, fecha_2):
    diferencia = fecha_2 - fecha_1
    resultado = diferencia.days * 24 * 3600 + diferencia.seconds
    return resultado

fecha_1 = datetime(2019, 1, 1)
fecha_2 = datetime.now()

print('Fecha actual:', fecha_2)

print(diferencia_segundos_fechas(fecha_1, fecha_2))
