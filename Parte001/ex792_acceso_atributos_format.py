# Ejercicio 792: Usar accesores de una estructura de datos en una cadena de formato.

persona = {'nombre': 'Daniela', 'apellido': 'Ortiz', 'edad': 29}

print(persona)

print()

print('{p[nombre]} - {p[apellido]} - {p[edad]}'.format(p=persona))
print('Nombre: {p[nombre]} - Apellido: {p[apellido]} - Edad: {p[edad]}'.format(p=persona))
