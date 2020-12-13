# Ejercicio 913: Obtener el máximo actual desde una colección (iterable) usando la función accumulate().

from itertools import accumulate

# running minimum
# running maximum

# (2, 3, 5, 0, 13, 11, 7, 19, 5, 2)
# 2, 3, 5, 5, 13, 13, 13, 19, 19, 19

def maximo_actual(numeros):
    return accumulate(numeros, max)

resultado = maximo_actual((2, 3, 5, 0, 13, 11, 7, 19, 5, 2))

print(type(resultado))

for m in resultado:
    print(m, end=' ')

print()
print()

resultado = maximo_actual([2, 3, 5, 0, 13, 11, 7, 19, 5, 2])

print(type(resultado))

for m in resultado:
    print(m, end=' ')
