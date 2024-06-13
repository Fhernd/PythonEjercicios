# Ejercicio 963: Obtener los valores del producto mínimo y máximo de un conjunto de datos numéricos.

from itertools import combinations

def valores_min_max_producto(numeros):
    minimo = min(combinations(numeros, 2), key=lambda s: s[0] * s[1])
    maximo = max(combinations(numeros, 2), key=lambda s: s[0] * s[1])

    return minimo, maximo

numeros = [2, 3, 5, 11, 19, 17, 2, 3, 7]

# minimo = (2, 2)
# maximo = (11, 17)

resultado = valores_min_max_producto(numeros)
print(resultado)
