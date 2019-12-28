# Ejercicio 395: Ordenar las listas de valores de las llaves de un diccionario.

numeros = {'l1': [5, 3, 7], 'l2': [-7, -9, 0], 'l3': [13, 12, 9]}
print(numeros)

numeros = {k: sorted(v) for k, v in numeros.items()}
print(numeros)
