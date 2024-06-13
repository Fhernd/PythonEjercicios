# Ejercicio 974: Generar los valores parciales de la serie factorial usando chain() y accumulate().

# 5! => [1, 1, 2, 6, 24, 120] <
# 7! => [1, 1, 2, 6, 24, 120, 720, 5040]

from itertools import accumulate, chain
from operator import mul

def valores_parciales_factorial(n):
    if not isinstance(n, int):
        raise TypeError('El argumento debe ser un número entero.')
    
    if n < 0:
        raise Exception('El argumento debe ser un número entero positivo (>=0).')

    resultado = list(accumulate(chain([1], range(1, n + 1)), mul))

    return resultado

print(valores_parciales_factorial(5)) # [1, 1, 2, 6, 24, 120]
print(valores_parciales_factorial(7)) # [1, 1, 2, 6, 24, 120, 720, 5040]
print(valores_parciales_factorial(11)) # [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, ...]
