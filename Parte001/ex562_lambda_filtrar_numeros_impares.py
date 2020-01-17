# Ejercicio 562: Crear una función lambda para filtrar números impares de una lista.

numeros = list(range(1, 11))
print(numeros)

print()

impares = list(filter(lambda n: n % 2 != 0, numeros))
print(impares)
