# Ejercicio 966: Obtener la frecuencia de los elementos de los grupos identificados con groupby().

from itertools import groupby

def conteo_frecuencia(datos):
    resultado = [sum(1 for c in d) for _, d in groupby(datos)]

    return resultado

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print(conteo_frecuencia(numeros)) # [1, 2, 3, 4, 5]

print()

numeros = [1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5]
print(conteo_frecuencia(numeros)) # [1, 2, 1, 4, 3]
