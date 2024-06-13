# Ejercicio 935: Usar la función accumulate() de itertools para multiplicar los valores de una lista.

from itertools import accumulate
from operator import mul

primos = [2, 3, 5, 7, 11]

resultado = list(accumulate(primos, mul))

print(resultado) # 2 6 30 210 2310

print()

producto = resultado[-1]
print(producto)

print()

resultado = list(accumulate(primos, mul, initial=100))

print(resultado) # 100 200 600 3000 21000 231000
