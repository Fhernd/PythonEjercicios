# Ejercicio 873: Comprobar si una cadena contiene un número decimal con precisión de 2.

import re

def es_decimal(cadena):
    patron = r'^[0-9]+(\.[0-9]{2})$'
    
    regex = re.compile(patron)

    return bool(regex.search(cadena))

print(es_decimal('987.1'))
print(es_decimal('987.12'))
print(es_decimal('98789877545.123'))
print(es_decimal('987.99'))
