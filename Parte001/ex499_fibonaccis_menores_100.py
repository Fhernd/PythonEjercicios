# Ejercicio 499: Generar los números de la serie Fibonacci menores a 100.

a, b = 0, 1

while b < 100:
    print(b)

    a, b = b, a + b
