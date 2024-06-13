# Ejercicio 355: Convertir una cadena que representa un diccionario en un objeto dict.

import ast

persona = "{'nombre': 'Oliva', 'email': 'oliva@mail.co', 'edad': 37}"

print(type(persona))
print(isinstance(persona, dict))
print(isinstance(persona, str))

print()

resultado = ast.literal_eval(persona)

print(type(resultado))
print(isinstance(resultado, dict))
print(isinstance(resultado, str))

print()

print(persona)
print(resultado)
