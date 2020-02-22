# Ejercicio 663: Convertir segundos del tiempo Unix a un objeto fecha con fromtimestamp().

import datetime

segundos_unix = 1435554000

fecha = datetime.datetime.fromtimestamp(segundos_unix)

print(type(fecha))
print(fecha)
