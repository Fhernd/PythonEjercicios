# Ejercicio 561: Crear una función lambda para filtrar los números pares de una lista.

numeros = list(range(1, 11))
print(numeros)

print()

pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares)
