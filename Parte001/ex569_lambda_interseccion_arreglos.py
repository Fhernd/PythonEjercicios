# Ejercicio 569: Crear una función lambda para calcular la intersección entre dos arreglos.

numeros_1 = [2, 3, 5, 7, 11, 13]
numeros_2 = [1, 4, 5, 3, 11, 10, 19, 23]

print(numeros_1)
print(numeros_2)

print()

resultado = list(filter(lambda n: n in numeros_1, numeros_2))
print(resultado)
