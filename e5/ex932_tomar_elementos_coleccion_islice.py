# Ejercicio 932: Tomar elementos de datos de una colección con la funcion islice() de itertools.

from itertools import islice

letras = 'ABCDEFGHIJKLM'

resultado = list(islice(letras, 2))
print(resultado)

print()

resultado = list(islice(letras, 2, len(letras), 2))
print(resultado)

print()

resultado = list(islice(letras, 2, 8, 2))
print(resultado)

print()

resultado = list(islice(letras, 2, None))
print(resultado)
