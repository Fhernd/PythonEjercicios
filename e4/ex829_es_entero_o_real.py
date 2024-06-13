# Ejercicio 829: Comprobar si una cadena de caracteres representa un número entero o real.

import re

def es_numero(cadena):
    patron = r'^(\d+(\.\d+)?)$'

    return bool(re.search(patron, cadena))

texto = '123a'
print(es_numero(texto))

print()

texto = '123'
print(es_numero(texto))

print()

texto = '123.'
print(es_numero(texto))

print()

texto = '123.456a'
print(es_numero(texto))

print()

texto = '123.456'
print(es_numero(texto))
