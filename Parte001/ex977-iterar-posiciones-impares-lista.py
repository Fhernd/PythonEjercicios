# Ejercicio 977: Iterar las posiciones impares de una lista en un ciclo for y while.

numeros = list(range(1, 11))
print(numeros)

print()

# [2, 4, 6, 8, 10]

print('Iteración con ciclo for:')

for i in range(1, len(numeros), 2):
    print(numeros[i], end=' ')

print()
print()

print('Iteración con ciclo while:')

i = 1

while i < len(numeros):
    print(numeros[i], end=' ')
    i += 2
