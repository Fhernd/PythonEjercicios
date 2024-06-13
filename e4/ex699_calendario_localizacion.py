# Ejercicio 699: Mostrar calendario para un lugar (locale) específico.

import calendar

calendario = calendar.LocaleTextCalendar(locale='en_CA.utf8')
calendario.prmonth(2020, 2)
