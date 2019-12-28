# Ejercicio 214: Contar el número de ocurrencias por cada carácter de un texto.

from collections import Counter

def contador_ocurrencias(cadena):
    ocurrencias = {}

    for c in cadena:
        if c in ocurrencias.keys():
            ocurrencias[c] += 1
        else:
            ocurrencias[c] = 1

    return ocurrencias

texto = '¡Python es génial!'

c = Counter(texto)

print(c)

print()

print(contador_ocurrencias(texto))
