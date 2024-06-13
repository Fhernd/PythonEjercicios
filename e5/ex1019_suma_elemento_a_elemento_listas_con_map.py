# Ejercicio 1019: Sumar elemento a elemento los datos de dos listas con la función map().

# [1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10]
# [7, 9, 11, 13, 15]

numeros_1 = [1, 2, 3, 4, 5]
numeros_2 = [6, 7, 8, 9, 10]

resultado = list(map(lambda x, y: x + y, numeros_1, numeros_2))
print(resultado)
