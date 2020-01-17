# Ejercicio 563: Crear una función lambda para generar números cuadrados.

numeros = list(range(1, 11))
print(numeros)

print()

cuadrados = list(map(lambda n: n ** 2, numeros))
print(cuadrados)
