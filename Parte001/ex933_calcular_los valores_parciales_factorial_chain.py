# Ejercicio 933: Calcular los valores parciales de la serie factorial usando el módulo itertools.

from itertools import accumulate, chain
from operator import mul

def factoriales(n):
    resultado = accumulate(chain([1], range(1, n + 1)), mul)

    return list(resultado)

print(factoriales(5)) # 1, 1, 2, 6, 24, 120

print()

print(factoriales(10))

print()

print(factoriales(50))
