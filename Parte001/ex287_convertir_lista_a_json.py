# Ejercicio 287: Convertir una lista de cadenas a formato JSON con el módulo json.

import json

lenguajes = ['Python', 'Java', 'C#', 'JavaScript', 'PHP']

print(lenguajes)
print(type(lenguajes))

datos_json = json.dumps(lenguajes)

print(datos_json)
print(type(datos_json))
