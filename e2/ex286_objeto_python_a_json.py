# Ejercicio 286: Convertir un objeto Python a datos en formato JSON con el módulo json.

import json

objeto = {'nombre': 'Edward', 'apellido': 'Ortiz', 'edad': 29}

print(type(objeto))

datos_json = json.dumps(objeto)

print(datos_json)
print(type(datos_json))
