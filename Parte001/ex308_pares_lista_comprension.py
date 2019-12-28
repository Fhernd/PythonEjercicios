# Ejercicio 308: Obtener los pares de un grupo de números usando una lista de comprensión.

numeros = list(range(1, 11))

print(numeros)

pares = [numero for numero in numeros if numero % 2 == 0]

print(pares)
