# Ejercicio 791: Cadena de formato con placeholders (receptáculos) para atributos de datos.

persona = {'nombre': 'Daniela', 'apellido': 'Ortiz', 'edad': 29}

print(persona)

print()

# Mecanismo tradicional:
print('Nombre: %(nombre)s - Apellido: %(apellido)s - Edad: %(edad)d' % persona)
print('Nombre: %(nombre)s - Edad: %(edad)d - Apellido: %(apellido)s' % persona)

print()

# Mecanismo nuevo (format()):
print('{nombre} - {apellido} - {edad}'.format(**persona))
print('{nombre} - {edad} - {apellido}'.format(**persona))
print('Nombre: {nombre} - Edad: {edad} - Apellido: {apellido}'.format(**persona))

print()

print('Nombre: {nombre} - Apellido: {apellido}'.format(nombre=persona['nombre'], apellido=persona['apellido']))
print('Nombre: {name} - Apellido: {lastname}'.format(name=persona['nombre'], lastname=persona['apellido']))

print()

print('Nombre: {nombre} - Apellido: {apellido}'.format(apellido='Ortiz', nombre='Daniela'))
