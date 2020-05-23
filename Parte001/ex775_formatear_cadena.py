# Ejercicio 775: Usar el operador % para pasar argumentos a una cadena de formato.

nombre = 'Edward'
apellido = 'Ortiz'
edad = 29

print('Nombre: ' + nombre + " - Apellido: " + apellido + " - Edad: " + str(edad))

print()

print('Nombre:', nombre, '- Apellido:', apellido, '- Edad:', edad)

print()

print('Nombre: %s - Apellido: %s - Edad: %i' % (nombre, apellido, edad))
