# Ejercicio 534: Crear la tabla de multiplicar (desde 1 hasta 10) para un x número.

numero = int(input('Digite un número entero: '))

for i in range(1, 11):
    print(f'{i} x {numero} = {i * numero}')
