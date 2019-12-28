# Ejercicio 184: Uso de la función accumulate de itertools en Python 3.8.0.

from itertools import accumulate

numeros = [2, 3, 5, 7]

print(list(accumulate(numeros)))

print(list(accumulate(numeros, initial=0)))

print(list(accumulate(numeros, initial=2000)))
