# Ejercicio 1029: Usar la fórmula de Gauss para sumar los números desde 1 hasta n.

# n(n + 1) / 2

while True:
    try:
        n = int(input('Digite el valor para n: '))

        if n > 1:
            break
        else:
            print('MENSAJE: Debe digitar un número entero positivo.')
    except ValueError:
        print('MENSAJE: Debe escribir un número entero válido.')

    print()

suma = n * (n + 1) / 2
print(f'La suma desde 1 hasta {n} es igual a {suma}.')

print()

print(sum(range(1, n + 1)))
