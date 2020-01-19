# Ejercicio 599: Ordenar una lista de números con la función bisect().

from bisect import bisect, insort

def ordenar(lista):
    lista_ordenada = []

    for e in lista:
        posicion = bisect(lista_ordenada, e)
        insort(lista_ordenada, e)

    return lista_ordenada


numeros = [7, 2, 13, 5, 17, 19, 3, 11]
print(numeros)

resultado = ordenar(numeros)
print(resultado)
