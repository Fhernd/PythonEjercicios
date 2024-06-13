# Ejercicio 254: Comprobar si una cadena de caracteres contiene todos los caracteres del alfabeto.

from string import ascii_lowercase

def validar_caracteres(cadena):
    return set(cadena) >= set(ascii_lowercase)


texto = 'The quick brown fox jumps over the lazy dgo'
print(validar_caracteres(texto))

texto = 'The quick brown fox jumps over the lazy cat'
print(validar_caracteres(texto))
