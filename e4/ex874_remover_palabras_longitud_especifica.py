# Ejercicio 874: Remover desde un texto aquellas palabras que tengan una longitud específica.

import re

def remover_palabras(texto, cantidad_caracteres):
    patron = '\\b\\w{%d}\\b' % (cantidad_caracteres)

    regex = re.compile(patron)

    return regex.sub('', texto)

cadena = 'Python es un lenguaje de programación multiparadigma.'
longitud = 2

print(cadena)

print()

resultado = remover_palabras(cadena, longitud)

print(resultado)

resultado = re.sub('\s+', ' ', resultado)

print(resultado)
