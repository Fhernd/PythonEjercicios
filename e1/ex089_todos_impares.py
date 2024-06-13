# Ejercicio 89: Generar números aleatorios y verificar que todos sean impares.

from random import randint


def generar_impares(n=5):
    impares = []

    while True:
        numeros = [randint(1, 10) for _ in range(n)]

        if all(x % 2 == 1 for x in numeros):
            impares = numeros
            break
    
    return impares


impares = generar_impares()

print(impares)

print(generar_impares(20))
