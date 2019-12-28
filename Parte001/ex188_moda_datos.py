# Ejercicio 188: Calcular la moda de un conjunto de datos numéricos y nominales.

from statistics import mode

numeros = [3, 2, 7, 2, 3, 2, 5, 11, 13, 2]

print(mode(numeros))

lenguajes = ['Python', 'C++', 'C++', 'Java', 'Python', 'C', 'JavaScript', 'Java', 'Python', 'Python']

print(mode(lenguajes))

numeros.append(3)
numeros.append(3)

print(mode(numeros))
