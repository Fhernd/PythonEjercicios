# Ejercicio 332: Generar un identificador único y variable para números y cadenas.

numero = 100
identificador = format(id(numero), 'x')
print(identificador)

print()

cadena = 'Python'
identificador = format(id(cadena), 'x')
print(identificador)
