# Ejercicio 807: Tomar un valor al azar desde una lista con la función shuffle().

from random import shuffle

numeros = list(range(1, 101))

print(numeros)

print()

shuffle(numeros)

print(numeros)

print()

numero = numeros.pop()

print(numero)
