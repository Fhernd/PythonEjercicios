# Ejercicio 290: Leer un archivo en formato JSON por medio de la función json.load().

import json

with open('Parte001/paises_capitales.json') as f:
    paises = json.load(f)

print(type(paises))
print(len(paises))

print(paises)

print()

print(paises[0])
print(type(paises[0]))
