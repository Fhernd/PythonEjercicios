# Ejercicio 114: Usar la función filter para obtener los números positivos de una lista.

numeros = [-2, 4, -8, 5, 7, 9, -10, -13]

positivos = list(filter(lambda x: x >= 0, numeros))

print(positivos)
