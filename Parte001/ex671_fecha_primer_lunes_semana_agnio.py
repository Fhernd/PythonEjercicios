# Ejercicio 671: Obtener la fecha del primer lunes del número de una semana específica.

import time

numero_semana = 8
fecha = time.asctime(time.strptime('2020 8 1', '%Y %W %w'))

print('Fecha primer lunes semana número 8:', fecha)
print(type(fecha))
