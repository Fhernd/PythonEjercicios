# Ejercicio 1001: Ordenar una lista de números a partir del módulo calculado por cada número.

# [101, 203, 105, 100, 53]
# => [1, 3, 0, 0, 3]
# => [105, 100, 101, 203, 53]

numeros = [101, 203, 105, 100, 53]
print(numeros)

print()

# Orden ascendente:
numeros_ordenados = sorted(numeros, key=lambda n: n % 5)
print(numeros_ordenados)

print()

# Orden descendente:
numeros_ordenados = sorted(numeros, key=lambda n: n % 5, reverse=True)
print(numeros_ordenados)
