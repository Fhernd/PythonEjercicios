# Ejercicio 665: Convertir un objeto date a un objeto datetime con combine().

from datetime import date, datetime

hoy = date.today()

print(type(hoy))
print(hoy)

print()

dt = datetime.combine(hoy, datetime.min.time())

print(type(dt))
print(dt)
