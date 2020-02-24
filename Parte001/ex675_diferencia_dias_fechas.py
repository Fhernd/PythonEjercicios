# Ejercicio 675: Diferencia en días entre dos fechas (objetos date).

from datetime import date

fecha_1 = date(2010, 1, 1)
fecha_2 = date(2020, 1, 1)

diferencia = fecha_2 - fecha_1

print(f'Diferencia total en días: {diferencia.days}')
