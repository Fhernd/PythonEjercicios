# Ejercicio 781: Utilizar el especificador de formato % sobre cadenas de caracteres.

nombre = 'Daniela Ortiz'
edad = 29
ahorros = 10000.79
casada = False

print('Nombre: ' + nombre + ' - Edad: ' + str(edad) + ' - Ahorros: $' + str(ahorros) + ' - Casada: ' + str(casada))

print()

print('Nombre: %s - Edad: %i - Ahorros: $%.2f - Casada: %s' % (nombre, edad, ahorros, casada))
