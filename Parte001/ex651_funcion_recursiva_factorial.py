# Ejercicio 651: Crear una función recursiva para calcular el factorial de un número.

# 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120
print(factorial(6)) # 720
print(factorial(7)) # 5040
