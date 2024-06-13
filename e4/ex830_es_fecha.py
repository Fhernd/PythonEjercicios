# Ejercicio 830: Comprobar si un cadena de caracteres es una fecha con formato AAAA/MM/DD.

import re

def es_fecha_valida(cadena):
    patron = '^20[0-9]{2}/(0\d|1[0-2])/(0\d|1[0-9]|2[0-9]|3[0-1])$'

    return bool(re.search(patron, cadena))

fecha = '2001/01/01'
print(es_fecha_valida(fecha))

print()

fecha = '1984/01/01'
print(es_fecha_valida(fecha))

print()

fecha = '2184/01/01'
print(es_fecha_valida(fecha))

print()

fecha = '2020/13/01'
print(es_fecha_valida(fecha))

print()

fecha = '2020/12/01'
print(es_fecha_valida(fecha))

print()

fecha = '2020/12/32'
print(es_fecha_valida(fecha))
