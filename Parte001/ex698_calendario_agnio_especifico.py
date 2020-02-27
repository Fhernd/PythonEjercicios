# Ejercicio 698: Generar el calendario completo (12 meses) para un año particular.

import calendar

calendario = calendar.TextCalendar(calendar.SUNDAY)

print(calendario.formatyear(2020, 2, 1, 1, 3))
