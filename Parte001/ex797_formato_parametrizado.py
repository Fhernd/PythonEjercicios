# Ejercicio 797: Parametrizar los especificadores de formato en una cadena.

lenguaje = 'Python'

print(lenguaje)
print('{:^10}'.format(lenguaje))

print()

padding = 10
print('{:^{p}}'.format(lenguaje, p=padding))

print()

alineacion = '>'
print('{:{a}{p}}'.format(lenguaje, p=padding, a=alineacion))

print()

alineacion = '<'
print('{:{a}{p}}'.format(lenguaje, p=padding, a=alineacion))
