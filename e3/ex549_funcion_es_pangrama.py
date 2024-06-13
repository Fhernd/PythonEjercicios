# Ejercicio 549: Crear una función personalizada para comprobar si una frase es un pangrama.

from string import ascii_lowercase

def es_pangrama(frase):
    conjunto = set(ascii_lowercase)

    return conjunto <= set(frase.lower())


cadena = 'The quick brown fox jumps over the lazy dog'
print(es_pangrama(cadena))

print(es_pangrama('Python es un lenguaje de programación multiparadigma'))
