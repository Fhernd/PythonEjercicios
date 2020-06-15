# Ejercicio 840: Comprobar si una cadena de caracteres empieza con un número.

import re

def empieza_con_numero(cadena):
    patron = '^[0-9]'

    return bool(re.search(patron, cadena))

texto = 'Python es tremendo'
print(empieza_con_numero(texto))

print()

texto = ' 5 lenguajes de programación'
print(empieza_con_numero(texto))

print()

texto = '\t5 lenguajes de programación'
print(empieza_con_numero(texto))

print()

texto = '5 lenguajes de programación'
print(empieza_con_numero(texto))
