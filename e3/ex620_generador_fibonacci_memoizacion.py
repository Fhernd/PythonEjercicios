# Ejercicio 620: Crear generador de la serie Fibonacci usando memoización.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

def fibonacci(n):
    if n == 0:
        serie_fibonacci = []
    elif n == 1:
        serie_fibonacci = [1]
    elif n == 2:
        serie_fibonacci = [0, 1]
    elif n > 2:
        serie_fibonacci = [0, 1]
        i = 1

        while i < n - 1:
            serie_fibonacci.append(serie_fibonacci[i] + serie_fibonacci[i - 1])
            i += 1
    
    return serie_fibonacci


resultado = fibonacci(11)
print(len(resultado))
print(resultado)
