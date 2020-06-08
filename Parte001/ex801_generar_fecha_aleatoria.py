# Ejercicio 801: Generar una fecha aleatoria para el año en curso.

from datetime import date
from random import randint

def fecha_aleatoria():
    fecha_inicio = date.today().replace(day=1, month=1).toordinal()
    fecha_final = date.today().toordinal()

    fecha = date.fromordinal(randint(fecha_inicio, fecha_final))

    return fecha

for _ in range(10):
    print(fecha_aleatoria())
