# Ejercicio 407: Crear un Objeto Diccionario a partir de un Archivo JSON.

import json

with open('Parte001/programacion.json', 'r') as f:
    programacion = json.load(f)

    print(type(programacion))
    print(programacion)
