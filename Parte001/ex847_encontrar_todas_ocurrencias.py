# Ejercicio 847: Encontrar todas las ocurrencias de una palabra en una frase.

import re

frase = 'Ejercicios Python, Curso Python, Laboratorio Python'
palabra = 'Python'

for r in re.findall(palabra, frase):
    print('Encontrado: %s' % r)
