# Ejercicio 597: Crear una entidad tipo namedtuple para representar datos de una persona.

from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'apellido', 'edad', 'email'])

edward = Persona('Edward', 'Ortiz', 29, 'edward@mail.co')

print(edward)
print(edward.nombre)
print(edward.apellido)
print(edward.edad)
print(edward.email)
