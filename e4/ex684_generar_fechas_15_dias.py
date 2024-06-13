# Ejercicio 684: Generar hasta doce (12) fechas diferenciadas cada una por 15 días.

from datetime import date, timedelta

def generar_fechas(fecha_inicio, cantidad=12, dias_diferencia=15):
    fechas = []
    fechas.append(fecha_inicio)

    for _ in range(cantidad):
        fecha_inicio = fecha_inicio + timedelta(days=dias_diferencia)
        fechas.append(fecha_inicio)

    return fechas

fecha = date.today()
resultado = generar_fechas(fecha)

print('Fecha actual:', fecha)

for f in resultado:
    print(f)
