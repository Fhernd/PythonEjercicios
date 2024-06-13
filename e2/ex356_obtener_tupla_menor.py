# Ejercicio 356: Encontrar la tupla en una lista cuyo valor en el segundo índice es menor.


def tupla_menor(lista):
    return min(lista, key=lambda t: (t[1], -t[0]))


puntos = [(7, 3), (11, 1), (5, 3), (2, 7), (-2, -4), (0, 0)]

resultado = tupla_menor(puntos)

print(resultado)
