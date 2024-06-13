# Ejercicio 596: Localizar el punto de inserción de un elemento en una lista ordenada.

import bisect

def localizar_punto_insercion(lista, valor):
    indice = bisect.bisect_left(lista, valor)
    return indice


numeros = [2, 5, 7, 11]
numero = 3
print(localizar_punto_insercion(numeros, numero))

numero = 13
print(localizar_punto_insercion(numeros, numero))
