# Ejercicio 930: Contar los elementos de los grupos identificados por la función groupby() de itertools.

from itertools import groupby

def contar_elementos_grupos(iterable):

    return [(k, len(list(e))) for k, e in groupby(iterable)]


cadena = 'ABBBCCDDDDDDEEFGHHHHHH'

resultado = contar_elementos_grupos(cadena)

print(resultado)
