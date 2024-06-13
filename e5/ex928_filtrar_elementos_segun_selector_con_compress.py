# Ejercicio 928: Crear un iterador a partir de un filtro de selección sobre los elementos de una lista.

# 1. 'Python'
# 2. [1, 0, 1, 0, 0, 1]
# Resultado: Ptn (Lista)

from itertools import compress

iterable = 'Python'
selector = [1, 0, 1, 0, 0, 1]

resultado = list(compress(iterable, selector))
print(resultado)

print()

iterable = ['P', 'y', 't', 'h', 'o', 'n']

resultado = list(compress(iterable, selector))
print(resultado)
