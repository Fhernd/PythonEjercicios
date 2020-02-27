# Ejercicio 700: Generar el calendario de un año y mes específicos en formato HTML.

import calendar

calendario_html = calendar.HTMLCalendar(calendar.MONDAY)

print(calendario_html.formatmonth(2020, 2))
