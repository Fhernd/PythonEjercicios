# Ejercicio 334: Cambiar de posición cada n-ésimo elemento con el elemento n+1.

# [1, 2, 3, 4, 5, 6] => [2, 1, 4, 3, 6, 5]

from itertools import chain, zip_longest

def cambiar_posiciones(lista):
    return list(chain.from_iterable(zip_longest(lista[1::2], lista[::2])))


numeros = [1, 2, 3, 4, 5, 6]
resultado = cambiar_posiciones(numeros)
print(numeros)
print(resultado)

print()

numeros = [1, 2, 3]
resultado = cambiar_posiciones(numeros)
print(numeros)
print(resultado)
