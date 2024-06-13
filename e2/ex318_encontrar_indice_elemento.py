# Ejercicio 318: Usar list.index() para encontrar el índice de un elemento en una lista.

lenguajes = ['Python', 'C#', 'PHP', 'C++', 'JavaScript', 'C', 'Java']

indice = lenguajes.index('JavaScript')
print(indice)

indice = lenguajes.index('Python')
print(indice)

print()

try:
    indice = lenguajes.index('python')
    print(indice)
except ValueError as e:
    print('ERROR:', e)
