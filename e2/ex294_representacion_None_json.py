# Ejercicio 294: Representación de None en formato de datos JSON.

import json

persona = {'nombre': 'Edward', 'apellido': 'Ordoñez', 'edad': 29, 'email': None}

print(persona)

persona_json = json.dumps(persona)

print(persona_json)
