# Ejercicio 406: Guardar un objeto diccionario en un archivo JSON.

import json

programacion = {'lenguajes': [{'nombre': 'Python', 'version': '3.8.0'}, {'nombre': 'Java', 'version': '12'}, {'nombre': 'JavaScript', 'version': 'ES6'}, {'nombre': 'PHP', 'version': '7.1.2'}], 'ides': ['Visual Studio', 'Eclipse IDE', 'NetBeans IDE', 'PyCharm', 'PhpStorm']}

print(programacion)

print()

print(type(programacion))

with open('programacion.json', 'w') as f:
    json.dump(programacion, f, indent=4, sort_keys=True)
