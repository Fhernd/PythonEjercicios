# Ejercicio 401: Contar la cantidad de elementos de los valores de un diccionario.

numeros = {'a': [1, 2, 3], 'b': [2, 3, 5, 7], 'c': [0, 1]}

cantidad = sum(map(len, numeros.values()))

print(cantidad)
