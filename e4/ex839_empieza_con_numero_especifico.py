# Ejercicio 839: Comprobar que una cadena empiece con un número específico.

import re

def empieza_con_numero(cadena):
    patron = '^3'

    return bool(re.search(patron, cadena))

texto = 'TresCuatro'
print(empieza_con_numero(texto))

print()

texto = '2.1'
print(empieza_con_numero(texto))

print()

texto = ' 3.1'
print(empieza_con_numero(texto))

print()

texto = '\n3.1'
print(empieza_con_numero(texto))

print()

texto = '3.1'
print(empieza_con_numero(texto))
