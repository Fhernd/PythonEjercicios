# Ejercicio 921: Repetir n cantidad de veces una colección con la función tee() de itertools.

from itertools import tee

numeros = [1, 2, 3, 4, 5]
print(numeros)

print()

resultado = tee(numeros, 5)

for r in resultado:
    print(list(r))
