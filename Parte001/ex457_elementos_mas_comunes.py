# Ejercicio 457: Hallar los elementos más comunes y el número de ocurrencias en una colección.

from collections import Counter

frase = 'Python es un lenguaje de programación. Python versión 3.8.1. Python es uno de los lenguajes más utilizados para crear soluciones de software.'

contador = Counter(frase)

print(contador)

print()

print(contador.most_common(5))
