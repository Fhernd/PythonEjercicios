# Ejercicio 697: Generar calendario para un mes específico empezando desde el lunes.

import calendar

calendario = calendar.TextCalendar(calendar.MONDAY)

print('Primer mes del año 2020:')
calendario.prmonth(2020, 1)
