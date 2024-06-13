# Ejercicio 315: Calcular la diferencia de elementos entre dos listas.

numeros_1 = [1, 2, 3, 4, 5]
numeros_2 = [1, 2, 7, 5]

diferencia = set(numeros_1) - set(numeros_2)

print(diferencia)

print()

diferencia = set(numeros_2) - set(numeros_1)

print(diferencia)
