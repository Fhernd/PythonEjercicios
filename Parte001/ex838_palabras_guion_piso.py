# Ejercicio 838: Comprobar que una palabra esté compuesta por caracteres alfanuméricos y el carácter de guion al piso.

import re

def validar_palabra(palabra):
    patron = '^[a-zA-Z0-9_]+$'

    return bool(re.search(patron, palabra))


texto = 'Python 3.8.0'
print(validar_palabra(texto))

print()

texto = 'Python_3.8.0'
print(validar_palabra(texto))

print()

texto = 'Python_3_8_0'
print(validar_palabra(texto))

print()

texto = ' Python_3_8_0 '
print(validar_palabra(texto))
