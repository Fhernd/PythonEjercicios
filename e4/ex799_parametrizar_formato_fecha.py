# Ejercicio 799: Parametrizar la cadena de formato de un objeto de tipo fecha (datetime).

from datetime import datetime

fecha = datetime(2002, 10, 8, 13, 19, 23)

print(fecha)

print()

# Parametrizar la salida de una fecha:
print('{:{formatoFecha} {formatoHora}}'.format(fecha, formatoFecha='%Y/%m/%d', formatoHora='%H:%M'))
