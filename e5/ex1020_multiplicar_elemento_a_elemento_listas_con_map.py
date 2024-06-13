# Ejercicio 1020: Multiplicar elemento a elemento los datos de dos listas con la función map().

numeros_1 = [1, 2, 3, 4, 5]
numeros_2 = [6, 7, 8, 9, 10]

# [6, 14, 24, 36, 50]

resultado = list(map(lambda x, y: x * y, numeros_1, numeros_2))
print(resultado)
