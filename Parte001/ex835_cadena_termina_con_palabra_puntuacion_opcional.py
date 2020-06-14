# Ejercicio 835: Comprobar si un texto termina con una palabra y puntuación opcional.

import re

def termina_palabra_puntuacion(frase):
    patron = '[a-zA-Z]+\S*$'

    return bool(re.search(patron, frase))

texto = 'Python es un lenguaje de programación.'
print(termina_palabra_puntuacion(texto))

print()

texto = 'Python es un lenguaje de programación'
print(termina_palabra_puntuacion(texto))

print()

texto = 'Python es un lenguaje de programación '
print(termina_palabra_puntuacion(texto))

print()

texto = 'Python v. 3.8.0.'
print(termina_palabra_puntuacion(texto))
