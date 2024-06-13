# Ejercicio 940: Comprobar cuáles objetos de una lista son iguales a otro objeto con la función is_().

from operator import is_

class Persona:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

personas = []
personas.append(Persona(1001, 'Mario'))
personas.append(Persona(1002, 'Angela'))
personas.append(personas[0])
personas.append(Persona(1003, 'Fabián'))
personas.append(Persona(1004, 'Andrea'))
personas.append(personas[0])

primera_persona = personas[0]

resultado = list(filter(lambda p: is_(p, primera_persona), personas))

for r in resultado:
    print(r.id, r.nombre)

print()

print('Cantidad de elementos en el resultado:', len(resultado))
