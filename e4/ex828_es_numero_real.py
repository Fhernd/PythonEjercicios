# Ejercicio 828: Comprobar si una cadena de caracteres representa un número real.

import re

def es_real(cadena):
    patron = r'^-?[0-9]+\.[0-9]+$'

    return bool(re.search(patron, cadena))

texto = '123'
print(es_real(texto))

print()

texto = '123.456'
print(es_real(texto))

print()

texto = '-123'
print(es_real(texto))

print()

texto = '-123.456a'
print(es_real(texto))

print()

texto = '-123.456'
print(es_real(texto))
