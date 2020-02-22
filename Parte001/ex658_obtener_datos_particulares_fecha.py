# Ejercicio 658: Obtener las partes esenciales de una fecha con el módulo datetime.

import datetime

ahora = datetime.datetime.now()
print('Fecha y hora actuales:', ahora)

hoy = datetime.date.today()
print('Hoy:', hoy)

print()

print('Año:', hoy.strftime('%Y'))
print('Nombre del mes:', hoy.strftime('%B'))
print('Número de la semana en el año:', hoy.strftime('%W'))
print('Número del día de la semana:', hoy.strftime('%w'))
print('Número del día del año:', hoy.strftime('%j'))
print('Número del día en el mes:', hoy.strftime('%d'))
print('Nombre del día de la semana:', hoy.strftime('%A'))
