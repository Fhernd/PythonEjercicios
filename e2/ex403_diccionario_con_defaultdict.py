# Ejercicio 403: Crear un diccionario con defaultdict usando dos listas de valores.

from collections import defaultdict

letras = ['A', 'B', 'C', 'D']
numeros = [1, 2, 2, 3]

diccionario = defaultdict(set)

for l, n in zip(letras, numeros):
    diccionario[l].add(n)

print(diccionario)
