# Ejercicio 976: Iterar las posiciones pares de una lista en un ciclo for y while.

numeros = list(range(1, 11))
print(numeros)

print()

print('Iteración posiciones pares de la lista `numeros` utilizando un ciclo for:')

for i in range(0, len(numeros), 2):
    print(numeros[i], end=' ')

print()
print()

print('Iteración posiciones pares de la lista `numeros` utilizando un ciclo while:')

i = 0

while i < len(numeros):
    print(numeros[i], end=' ')

    i += 2
