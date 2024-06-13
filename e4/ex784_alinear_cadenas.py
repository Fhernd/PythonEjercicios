# Ejercicio 784: Alinear cadenas de caracteres con especificadores de formato y la función format().

lenguaje = 'Python'

print(lenguaje)

print()

# Alinear a la derecha (>):
print('{:>24}'.format(lenguaje))

print()

version = '3.8.1'

# Alinear a la izquierda:
print(lenguaje, version)

print('{:<12}{}'.format(lenguaje, version))

print()

print('{:_<12}{}'.format(lenguaje, version))

print()

# Centrar el texto:

print('{:^12}'.format(lenguaje))
print('{:#^12}'.format(lenguaje))
