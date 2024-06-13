# Ejercicio 843: Comprobar si una cadena de caracteres termina en un número cualquiera.

import re

def termina_en_numero(texto):
    patron = '[0-9]$'

    return bool(re.search(patron, texto))

texto = 'La versión mayor de Python es la número 3.'
print(termina_en_numero(texto))

print()

texto = 'La versión mayor de Python es la número 3\n'
print(termina_en_numero(texto))

print()

texto = 'La versión mayor de PHP es la número 7'
print(termina_en_numero(texto))

print()

texto = 'El primer entero negativo es -1'
print(termina_en_numero(texto))

print()

texto = 'El primer entero negativo es -1\t'
print(termina_en_numero(texto))
