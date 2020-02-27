# Ejercicio 696: Generar representación en cadena de caracteres de una fecha (datetime).

from datetime import datetime

ahora = datetime.now()
print(type(ahora))

ahora_cadena = ahora.strftime('%Y-%m-%d %H:%M:%S')
print(type(ahora_cadena))
print(ahora_cadena)
