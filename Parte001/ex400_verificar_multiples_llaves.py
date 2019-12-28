# Ejercicio 400: Comprobar si múltiples llaves existen en un diccionario.

persona = {'nombre': 'Edward', 'apellido': 'Ortiz', 'email': 'edward@mail.co', 'edad': 33}

print(persona.keys() >= {'nombre', 'edad'})
print(persona.keys() >= {'email', 'movil'})
print(persona.keys() >= {'email', 'apellido', 'edad'})
print(persona.keys() >= {'profesion'})
