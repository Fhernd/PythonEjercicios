# Ejercicio 571: Crear una función lambda para contar la cantidad de pares e impares.

numeros = list(range(1, 12))
print(numeros)

cantidad_pares = len(list(filter(lambda n: n % 2 == 0, numeros)))
cantidad_impares = len(list(filter(lambda n: n % 2 != 0, numeros)))

print(f'Cantidad de números pares: {cantidad_pares}')
print(f'Cantidad de números impares: {cantidad_impares}')
