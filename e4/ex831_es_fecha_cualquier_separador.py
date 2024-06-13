# Ejercicio 831: Comprobar si una cadena es una fecha (usar cualquier separador).Python - Ejercicio 831: Comprobar si una Cadena es una Fecha (Usar Cualquier Separador)

# AAAA-MM-DD
# AAAA/MM/DD
# AAAA.MM.DD

import re

def es_fecha_valida(cadena):
    patron = '^20[0-9]{2}(\.|/|-)(0\d|1[0-2])(\.|/|-)(0\d|1\d|2\d|3[0-1])$'

    return bool(re.search(patron, cadena))

fecha = '2020/06/13'
print(es_fecha_valida(fecha))

print()

fecha = '2020-06-13'
print(es_fecha_valida(fecha))

print()

fecha = '2020.06.13'
print(es_fecha_valida(fecha))

print()

fecha = '2020.13.13'
print(es_fecha_valida(fecha))

print()

fecha = '2020/06/43'
print(es_fecha_valida(fecha))
