# Ejercicio 826: Comprobar si una cadena de caracteres representa un número entero positivo.

import re

def es_numero_entero_positivo(cadena):
    patron = '^[0-9]+$'

    return bool(re.search(patron, cadena))

texto = '123a'
print(es_numero_entero_positivo(texto))

print()

texto = '123'
print(es_numero_entero_positivo(texto))

print()

texto = '-123'
print(es_numero_entero_positivo(texto))
