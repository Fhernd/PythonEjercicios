# Ejercicio 540: Crear una función recursiva para calcular el factorial de un número.

# 5! = 5 * 4 * 3 * 2 * 1 = 120

def factorial(n):
    # producto = 1
    # for i in range(1, n + 1):
    #     producto *= i
    
    # return producto
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
print(factorial(10))
