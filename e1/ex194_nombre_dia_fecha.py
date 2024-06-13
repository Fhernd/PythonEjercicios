# Ejercicio 194: Encontrar el nombre del día a partir de una fecha dada.

from datetime import date

print('Ingrese el número del mes y del día: ', end='')
mes, dia = map(int, input().split())

semana = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles', 4: 'Jueves', 5: 'Viernes', 6: 'Sábado', 7: 'Domingo'}

numero_dia = date.isoweekday(date(2019, mes, dia))

print('El nombre del día es: %s' % semana[numero_dia])
