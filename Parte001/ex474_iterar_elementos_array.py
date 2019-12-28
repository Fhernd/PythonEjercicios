# Ejercicio 474: Iterar todos los elementos de un objeto array con un ciclo for.

from array import array

numeros = array('i', [2, 3])

numeros.append(5)
numeros.append(7)
numeros.extend([11, 13, 17])

print(numeros)

for n in numeros:
    print(n)
