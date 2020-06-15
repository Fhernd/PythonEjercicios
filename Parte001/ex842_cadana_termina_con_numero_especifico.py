# Ejercicio 842: Comprobar si una cadena de caracteres termina con un número específico.

import re

def termina_en_numero(texto):
    patron = '3$'

    return bool(re.search(patron, texto))

cadena = 'Su número favorito es 7'
print(termina_en_numero(cadena))

print()

cadena = 'Su número favorito es 3.'
print(termina_en_numero(cadena))

print()

cadena = 'Su número favorito es 3\n'
print(termina_en_numero(cadena))

print()

cadena = 'Su número favorito es 3\t'
print(termina_en_numero(cadena))

print()

cadena = 'Su número favorito es 3'
print(termina_en_numero(cadena))
