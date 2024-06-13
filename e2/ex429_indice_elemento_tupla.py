# Ejercicio 429: Encontrar el índice de un elemento en una tupla.

lenguajes = ('Python', 'C#', 'JavaScript', 'C++', 'PHP')

indice = lenguajes.index('JavaScript')

print(indice)

try:
    indice = lenguajes.index('php')
    print(indice)
except ValueError as e:
    print('Ha ocurrido un error:', e)
