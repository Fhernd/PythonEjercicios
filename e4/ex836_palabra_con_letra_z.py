# Ejercicio 836: Comprobar si existe una palabra que contenga el carácter z.

import re

def frase_palabra_caracter_z(frase):
    patron = '\w*(z|Z).?\w*'

    return bool(re.search(patron, frase))

texto = 'Python es tremendo'
print(frase_palabra_caracter_z(texto))

print()

texto = 'John Ortiz'
print(frase_palabra_caracter_z(texto))

print()

texto = 'JOHN ORTIZ'
print(frase_palabra_caracter_z(texto))

print()

texto = 'El zorro es un animal.'
print(frase_palabra_caracter_z(texto))
