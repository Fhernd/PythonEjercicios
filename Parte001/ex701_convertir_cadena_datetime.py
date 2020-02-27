# Ejercicio 701: Convertir una cadena de caracteres de fecha en un objeto datetime.

from datetime import datetime

cadena_fecha = 'Jun 23 1912 3:31AM'

fecha = datetime.strptime(cadena_fecha, '%b %d %Y %I:%M%p')

print('Tipo de dato de la variable fecha:', type(fecha))
print(fecha)
