# Ejercicio 910: Crear un objeto iterable a partir de diferentes colecciones con itertools.chain().

from itertools import chain

numeros = [1, 2, 3]
letras = ['A', 'B', 'C', 'D', 'E']
primos = [11, 13, 17]

iterable = chain(numeros, letras, primos)

for e in iterable:
    print(e, end=' ')

print()
print()

iterable = chain(primos, numeros, letras)

for e in iterable:
    print(e, end=' ')

print()
print()

# Creación a partir de tuplas:
lenguajes = ('C', 'Go', 'PHP', 'C++')
paises = ('Colombia', 'Perú', 'Chile', 'Grecia', 'China')
ides = ('Visual Studio', 'Eclipse')

iterable = chain(lenguajes, paises, ides)

for e in iterable:
    print(e, end=' ')

print()

iterable = chain(paises, lenguajes, ides)

for e in iterable:
    print(e, end=' ')

print()

# Diferentes argumentos para la función chain():
iterable = chain(primos, lenguajes)
for e in iterable:
    print(e, end=' ')

print()
print()

nombre = 'Sonia'

iterable = chain(lenguajes, primos, nombre)
for e in iterable:
    print(e, end=' ')
