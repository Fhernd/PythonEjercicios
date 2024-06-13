# Ejercicio 92: Filtrar números por medio de la función filter.

numeros = [i for i in range(10)]

print(numeros)

filtro_impares = lambda x: x % 2 == 1

impares = filter(filtro_impares, numeros)

print(list(impares))
