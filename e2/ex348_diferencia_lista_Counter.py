# Ejercicio 348: Calcular la diferencia de dos listas usando la clase Counter.

from collections import Counter

lenguajes_1 = ['Python', 'C#', 'JavaScript', 'PHP']
lenguajes_2 = ['C++', 'Python', 'Java', 'C', 'Go']

contador_1 = Counter(lenguajes_1)
contador_2 = Counter(lenguajes_2)

print(contador_1)
print(contador_2)

print()

resultado = contador_1 - contador_2
print(resultado)

print()

resultado = contador_2 - contador_1
print(resultado)
