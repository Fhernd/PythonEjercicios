# Ejercicio 291: Crear un nuevo archivo JSON a partir de uno ya existente.

import json

with open('Parte001/paises_capitales.json') as f:
    paises_capitales = json.load(f)

print(len(paises_capitales))

print(paises_capitales[0])

for p in paises_capitales:
    del p['city']

print()

print(len(paises_capitales))

print(paises_capitales[0])

with open('Parte001/paises.json', 'w') as f:
    json.dump(paises_capitales, f, indent=4)
