# Ejercicio 673: Crear una función para sumar n cantidad de años a una fecha.

import datetime
from datetime import date

def sumar_agnios(fecha, agnios):
    try:
        return fecha.replace(year = fecha.year + agnios)
    except ValueError:
        return fecha + (date(fecha.year + agnios, 1, 1) - date(fecha.year, 1, 1))

fecha = date(2020, 1, 13)
print(sumar_agnios(fecha, 2))
print(sumar_agnios(fecha, -2))

print()

fecha = date(2020, 2, 29)
print(sumar_agnios(fecha, 1))
print(sumar_agnios(fecha, 4))
