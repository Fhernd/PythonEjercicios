# Ejercicio 204: Sumar todos los dígitos que aparezcan en una cadena de caracteres.

# Solución:

# Python 3.8.0 es la versión más reciente de este lenguaje de programación.

import re


def sumar_digitos_cadena(cadena):
    patron = r'[0-9]{1,7}'
    numeros = re.findall(patron, cadena)
    numeros = map(int, numeros)

    return sum(numeros)


texto = 'Python 3.8.0 es la versión más reciente de este lenguaje de programación.'

print(sumar_digitos_cadena(texto))

texto = 'Python es génial. La versión mayor más reciente es 3. El número de mejor es 8.'

print(sumar_digitos_cadena(texto))

texto = 'ABC123XYZ7'

print(sumar_digitos_cadena(texto))
