# Ejercicio 832: Comprobar si una cadena empieza con a y termina con b.

# a...b

import re

def es_cadena_valida(cadena):
    patron = '^a.*?b$'

    return bool(re.search(patron, cadena))

texto = 'aadddd,,,,,d'
print(es_cadena_valida(texto))

print()

texto = 'ad'
print(es_cadena_valida(texto))

print()

texto = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaassssssssssssssssssssssssssssssssb'
print(es_cadena_valida(texto))

print()

texto = 'a@     -#sslkñsklsjkljlksjklkljsb'
print(es_cadena_valida(texto))
