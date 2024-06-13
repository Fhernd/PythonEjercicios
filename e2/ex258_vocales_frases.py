# Ejercicio 258: Obtener y contar las vocales que tiene una frase.


def obtener_vocales(frase):
    vocales = 'aeouiAEOUI'

    return set([c for c in frase if c in vocales])


texto = 'Python es genial'

print(obtener_vocales(texto))
print(len(obtener_vocales(texto)))
