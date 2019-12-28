# Ejercicio 456: Repetir un elemento cierta cantidad de veces con la clase Counter.

from collections import Counter

contador = Counter(a=5, e=4, i=0, o=-1, u=2)

print(contador)
print()

elementos_repetidos = list(contador.elements())

print(type(elementos_repetidos))
print(elementos_repetidos)
