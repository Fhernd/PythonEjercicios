# Ejercicio 833: Comprobar si un texto empieza con una palabra por medio de una expresión regular.

import re

def empieza_con_palabra(frase):
    patron = '^[a-zA-Z]+'

    return bool(re.search(patron, frase))

texto = '¡Python es tremendo!'
print(empieza_con_palabra(texto))

print()

texto = 'Python es tremendo!'
print(empieza_con_palabra(texto))

print()

texto = ' Python es tremendo!'
print(empieza_con_palabra(texto))

print()

texto = '3Python es tremendo!'
print(empieza_con_palabra(texto))

print()

texto = 'python es tremendo!'
print(empieza_con_palabra(texto))

print()

texto = '@Python es tremendo!'
print(empieza_con_palabra(texto))
