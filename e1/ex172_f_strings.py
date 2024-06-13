# Ejercicio 172: Explorar el nuevo soporte para depuración por medio de f-strings de Python 3.8.0.

import datetime

nombre = 'Daniela Ortiz'
fecha = datetime.datetime.now()

print('nombre=', nombre)
print('fecha=', fecha)

print()

# Uso de f-strings:

print(f'{nombre=}')
print(f'{fecha=}')

print()

fecha_nacimiento = datetime.date(1993, 10, 2)
hoy = datetime.date.today()
delta = hoy - fecha_nacimiento

print(f'{delta.days=:,d}')
