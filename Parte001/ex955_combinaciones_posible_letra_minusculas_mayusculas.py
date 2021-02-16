# Ejercicio 955: Obtener todas las combinaciones posibles de minúsculas y mayúsculas de un conjunto de caracteres.

from itertools import product

def obtener_combinaciones(caracteres):
    resultado = map(''.join, product(*((c.lower(), c.upper()) for c in caracteres)))

    return list(resultado)

frase = 'abc'

combinaciones = obtener_combinaciones(frase)

print(combinaciones)
