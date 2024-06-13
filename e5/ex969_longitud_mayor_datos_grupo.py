# Ejercicio 969: Obtener la mayor longitud de los grupos identificados por la función groupby().

from itertools import groupby

def mayor_longitud_grupo(texto):
    resultado = max(len(list(d)) for _, d in groupby(texto))

    return resultado

contenido = 'AAABBCCCCCDDD'
print(mayor_longitud_grupo(contenido))  # 5
