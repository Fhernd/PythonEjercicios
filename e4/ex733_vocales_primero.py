# Ejercicio 733: Crear una función para dejar las vocales de una palabra al principio.

def vocales_primero(palabra):
    vocales = [c for c in palabra if c in 'aeiouAEIOU']
    consonantes = [c for c in palabra if c not in 'aeiouAEIOU']

    return ''.join(vocales) + ''.join(consonantes)


palabra = 'vocales'
print(vocales_primero(palabra)) # oaevcls
palabra = 'Python'
print(vocales_primero(palabra)) # oPythn
