# Ejercicio 678: Crear una función para encontrar el último número de día de un mes y un año.

import calendar

def ultimo_numero_dia(mes, agnio):
    return calendar.monthrange(agnio, mes)

print(ultimo_numero_dia(2, 2020)[1])
print(ultimo_numero_dia(12, 2020)[1])
