# Ejercicio 693: Convertir diferencia en segundos de dos fechas en dias, horas, minutos.

from datetime import datetime

def diferencia_segundos_fechas(fecha_1, fecha_2):
    diferencia = fecha_2 - fecha_1
    resultado = diferencia.days * 24 * 3600 + diferencia.seconds
    return resultado

def dias_horas_minutos_segundos(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    dias, horas = divmod(horas, 24)

    return dias, horas, minutos, segundos

fecha_1 = datetime(2019, 1, 1)
fecha_2 = datetime.now()
print('Fecha actual:', fecha_2)
segundos = diferencia_segundos_fechas(fecha_1, fecha_2)
print(segundos)

print()

resultado = dias_horas_minutos_segundos(segundos)
print(resultado)
