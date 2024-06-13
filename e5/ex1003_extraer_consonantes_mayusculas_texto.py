# Ejercicio 1003: Extraer las consonantes mayúsculas desde un texto usando la función filter().

from string import ascii_uppercase

frase = 'Python Es Tremendo'
print(frase)

print()

print(ascii_uppercase)

letras = set(ascii_uppercase) - set('AEIOU')
print(letras)

print()

consonantes = list(filter(lambda c: c in letras, frase))
print(consonantes)
