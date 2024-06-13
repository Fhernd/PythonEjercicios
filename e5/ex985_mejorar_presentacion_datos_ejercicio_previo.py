# Ejercicio 985: Usar cadenas de formato para mejorar la presentación de datos del ejercicio no. 984.

from math import sqrt

while True:
    try:
        limite_inferior = int(input('Digite el valor para el límite inferior del rango: '))

        break
    except ValueError:
        print('ERROR: Debe digitar un número entero.')
    
    print()

print()

while True:
    try:
        limite_superior = int(input('Digite el valor para el límite superior del rango: '))

        if limite_superior <= limite_inferior:
            print('ADVERTENCIA: El límite superior debe ser mayor al límite inferior.')
            print()
            continue

        break
    except ValueError:
        print('ERROR: Debe digitar un número entero.')
    
    print()

print()

numeros = list(range(limite_inferior, limite_superior + 1))

print('{:>4}{:>12}{:>12}{:>12}'.format('n', 'Cuadrado', 'Cubo', 'Raíz'))
for n in numeros:
    print('{:4d}{:10d}{:12d}{:>15}'.format(n, n**2, n**3, round(sqrt(n), 2)))
