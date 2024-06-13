# Ejercicio 289: Convertir una lista en formato JSON en una lista Python con loads.

import json

arreglo_json = '["Python", "Java", "PHP", "C#", "PHP"]'

lista = json.loads(arreglo_json)

print(type(lista))
print(lista)
