# Ejercicio 975: Iterar una lista en sentido inverso con el ciclo for y usando la función range().

numeros = list(range(1, 11))
print(numeros)

print()

for i in range(len(numeros)):
    print(numeros[i], end=' ')

print()

for i in range(len(numeros) - 1, -1, -1):
    print(numeros[i], end=' ')
