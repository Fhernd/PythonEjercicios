# Ejercicio 912: Obtener el mínimo actual desde una colección (iterable) usando la función accumulate().

from itertools import accumulate

# (3, 2, 1, 7, 0, 11, 13, 5, -1, 17, 19)
# 3, 2, 1, 1, 0, 0, 0, -1, -1, -1

def minimo_actual(numeros):
    return accumulate(numeros, min)

resultado = minimo_actual((3, 2, 1, 7, 0, 11, 13, 5, -1, 17, 19))

for m in resultado:
    print(m, end=' ')

print()
print()

resultado = minimo_actual([3, 2, 1, 7, 0, 11, 13, 5, -1, 17, 19])

for m in resultado:
    print(m, end=' ')
