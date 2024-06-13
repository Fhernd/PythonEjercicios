# Ejercicio 191: Obtener múltiples modas desde un conjunto de datos numéricos o nominales.

from statistics import multimode

numeros = [0, 3, 2, 7, 2, 3, 2, 5, 11, 13, 2, 3, 3]

print(multimode(numeros))

lenguajes = ['Java', 'Python', 'C++', 'C++', 'Java', 'Python', 'C', 'JavaScript', 'Java', 'Python', 'Python', 'Java']

print(multimode(lenguajes))
