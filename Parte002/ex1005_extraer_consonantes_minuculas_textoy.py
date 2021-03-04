# Ejercicio 1005: Extraer las consonantes minúsculas desde un texto usando la función filter().

from string import ascii_lowercase

frase = 'Python Es Tremendo'
print(frase)

print()

print(ascii_lowercase)
letras = set(ascii_lowercase) - set('aeiou')

print()

consonantes_minusculas = list(filter(lambda c: c in letras, frase))
print(consonantes_minusculas)
