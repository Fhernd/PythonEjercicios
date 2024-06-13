# Ejercicio 850: Reemplazar espacio en blanco en una cadena con una expresión regular.

import re

frase = '      Python        es  un lenguaje        de programación                 .'

print(frase)

print(len(frase))
frase = frase.strip()[:-2].strip()

print(frase)

print()

remover_espacio_blanco = re.compile(r'\s+')

frase = remover_espacio_blanco.sub(' ', frase)

print(frase)
print(len(frase))
