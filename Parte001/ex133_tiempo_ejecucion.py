# Ejercicio 133: Calcular el tiempo de ejecución de una función.

from timeit import default_timer


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


inicio = default_timer()
fibonacci(20)
fin = default_timer()

print(fin - inicio)

print()

inicio = default_timer()
fibonacci(37)
fin = default_timer()

print(fin - inicio)
