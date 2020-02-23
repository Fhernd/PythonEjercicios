# Ejercicio 672: Obtener todas las fechas de los domingos de un año particular.

from datetime import date, timedelta

def generar_fecha_domingo(agnio):
    fecha = date(agnio, 1, 1)
    fecha += timedelta(days=6-fecha.weekday())

    while fecha.year == agnio:
        yield fecha
        fecha += timedelta(days=7)


for f in generar_fecha_domingo(2020):
    print(f)
