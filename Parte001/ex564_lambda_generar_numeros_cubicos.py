# Ejercicio 564: Crear una función lambda para generar números cúbicos.

numeros = list(range(1, 11))
print(numeros)

print()

cubicos = list(map(lambda n: n ** 3, numeros))
print(cubicos)
