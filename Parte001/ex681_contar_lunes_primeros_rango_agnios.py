# Ejercicio 681: Contar la cantidad de lunes que son el primer día de cada mes en un rango de años.

from datetime import datetime

def cantidad_lunes_primer_dia_mes(agnio_1, agnio_2):
    contador = 0

    for a in range(agnio_1, agnio_2 + 1):
        for m in range(1, 13):
            if datetime(a, m, 1).weekday() == 0:
                contador += 1
    
    return contador

agnio_1 = 2018
agnio_2 = 2020
resultado = cantidad_lunes_primer_dia_mes(agnio_1, agnio_2)
print(resultado)

print(cantidad_lunes_primer_dia_mes(2020, 2020))
