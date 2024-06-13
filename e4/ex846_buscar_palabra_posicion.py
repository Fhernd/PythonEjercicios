# Ejercicio 846: Encontrar una palabra e indicar su posición de inicio y final en una frase.

import re

frase = 'Python es un lenguaje de programación multiparadigma.'
palabra = 'lenguaje'

resultado = re.search(palabra, frase)

inicio = resultado.start()
final = resultado.end()

print('La palabra {} se encontró al inicio {} y final {}.'.format(palabra, inicio, final))
