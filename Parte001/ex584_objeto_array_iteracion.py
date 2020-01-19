# Ejercicio 584: Crear un objeto array e iterar cada uno de sus elementos en un ciclo for.

from array import array

numeros = array('i', [2, 3, 5, 7, 11, 13])

print(numeros)
print(type(numeros))

print()

for n in numeros:
    print(n)
