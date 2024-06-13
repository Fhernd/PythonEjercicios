# Ejercicio 12: Imprimir el calendario para un año y mes específicos.

import calendar

agnio = int(input('Escriba el año: '))
mes = int(input('Escriba el mes: '))

print(calendar.month(agnio, mes))
