# Ejercicio 1013: Ordenar una lista con la función sort() y una expresión lambda como llave de ordenamiento.

numeros = [13, 2, 19, 5, 7, 11, 17]
print(numeros)

print()

# [7, 50, 5, 20, 14, 9, 5]
# => [5, 5, 7, 9, 14, 20, 50]
numeros.sort(key=lambda n: 100/n)

print(numeros) # [19, 17, 13, 11, 7, 5, 2]
