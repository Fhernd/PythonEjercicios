# Ejercicio 848: Encontrar todas las ocurrencias de una palabra en una frase y su posición.

import re

frase = 'Ejercicios Python, Curso Python, Laboratorio Python'
palabra = 'Python'

for r in re.finditer(palabra, frase):
    inicio = r.start()
    final = r.end()
    palabra_encontrada = frase[inicio:final]

    print('Se ha encontrado la palabra `{}` en las posiciones desde {} hasta {}'.format(palabra_encontrada, inicio, final))
