# Ejercicio 651: Crear una función recursiva para calcular el enésimo valor de Fibonacci.

# 0 1 1 2 3 5 8 13 21 34 55 89, ...

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))
print(fibonacci(7))
print(fibonacci(9))
