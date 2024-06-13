# Ejercicio 309: Obtener los impares de un grupo de números usando una lista de comprensión.

numeros = list(range(1, 11))

print(numeros)

impares = [numero for numero in numeros if numero % 2 == 1]

print(impares)
