# Ejercicio 293: Decodificar un número complejo en formato JSON a objeto Python.

import json

def decodificar_numero_complejo(objeto):
    return complex(objeto['real'], objeto['imag'])


objeto = json.loads('{"real": 3, "imag": 6}', object_hook=decodificar_numero_complejo)

print(type(objeto))
print(objeto)
