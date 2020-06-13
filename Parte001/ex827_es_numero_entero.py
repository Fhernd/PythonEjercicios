# Ejercicio 827: Comprobar si una cadena de caracteres representa un número entero.

import re

def es_entero(cadena):
    patron = '^[-]{0,1}[0-9]+$'

    return bool(re.search(patron, cadena))

texto = '1000a'
print(es_entero(texto))

print()

texto = '1000'
print(es_entero(texto))

print()

texto = '-1000'
print(es_entero(texto))

print()

texto = '--1000'
print(es_entero(texto))

print()

texto = '1000.101'
print(es_entero(texto))
