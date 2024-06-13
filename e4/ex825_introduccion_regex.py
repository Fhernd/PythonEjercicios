# Ejercicio 825: Comprobar si una cadena de caracteres únicamente contiene ciertos caracteres.

import re

def contiene_caracteres(texto):
    patron = re.compile(r'[a-zA-Z0-9.]')

    return bool(patron.search(texto))


cadena = 'Python'
print(contiene_caracteres(cadena))

print()

cadena = '#@/-*'

print(contiene_caracteres(cadena))
