# Ejercicio 404: Sumar la lista de valores de cada llave de un objeto diccionario.

numeros = {'a': [1, 2, 3], 'b': [9, 8, 7], 'c': [2, 3, 5]}
print(numeros)

print()

numeros = {k: sum(v) for k, v in numeros.items()}
print(numeros)
