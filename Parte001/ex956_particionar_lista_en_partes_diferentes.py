# Ejercicio 956: Usar la función islice() de itertools para particionar una lista en un tamaño dado.

from itertools import islice

numeros = list(range(1, 21))
print(numeros)

print()

numeros_iterador = iter(numeros)

resultado = list(iter(lambda: tuple(islice(numeros_iterador, 3)), ()))
print(resultado)

print()

numeros_iterador = iter(numeros)
resultado = list(iter(lambda: tuple(islice(numeros_iterador, 5)), ()))
print(resultado)
