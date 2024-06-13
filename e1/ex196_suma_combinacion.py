# Ejercicio 196: Encontrar una combinación de tamaño n que sea igual a un valor.

from itertools import combinations


while True:
    print('Ingrese el tamaño de las combinaciones y el valor de la suma: ', end='')
    n, suma = map(int, input().split())

    if n == 0 and suma == 0:
        break

    combinaciones = list(combinations(range(10), n))

    for c in combinaciones:
        if sum(c) == suma:
            print(c, sum(c))
