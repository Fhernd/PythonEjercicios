# Ejercicio 285: Crear un objeto Python a partir de datos en formato JSON.

import json

datos_json = '{"nombre": "Edward", "apellido": "Ortiz", "edad": 29}'

objeto = json.loads(datos_json)

print(objeto)

print(objeto['nombre'])
print(objeto['apellido'])
print(objeto['edad'])

print()

print(type(objeto))
