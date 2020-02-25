# Ejercicio 677: Crear una función para determinar si una fecha es el tercer miércoles del mes.

import datetime

def es_tercer_miercoles(cadena):
    fecha = datetime.datetime.strptime(cadena, '%Y %m %d')
    return fecha.weekday() == 2 and 14 < fecha.day <= 22

print(es_tercer_miercoles('2020 02 17'))
print(es_tercer_miercoles('2020 02 19'))
print(es_tercer_miercoles('2020 01 22'))
