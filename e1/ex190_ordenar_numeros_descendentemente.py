# Ejercicio 190: Ordenar un conjunto de datos numéricos de forma descendente.

print('Digite seis números: ', end='')
numeros = list(map(int, input().split()))

print(numeros)

numeros.sort()

print(numeros)

numeros.reverse()

print(numeros)
