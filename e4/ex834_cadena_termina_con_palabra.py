# Ejercicio 834: Comprobar si un texto termina con una palabra por medio de una expresión regular.

import re

def termina_en_palabra(frase):
    patron = '[a-zA-Z]+$'

    return bool(re.search(patron, frase))


texto = 'Python 3.8.0'
print(termina_en_palabra(texto))

print()

texto = 'Python 3.8.0 es una de últimas versiones'
print(termina_en_palabra(texto))

print()

texto = 'John Ortiz Ordoñez'
print(termina_en_palabra(texto))

print()

texto = '¡Python es tremendo!'
print(termina_en_palabra(texto))
