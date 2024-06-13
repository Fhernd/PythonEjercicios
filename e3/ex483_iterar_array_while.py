# Ejercicio 483: Iterar los elementos de un objeto array con un ciclo while.

from array import array

numeros = array('i', [2, 3, 5, 7, 11, 13, 17, 19])

indice = 0

while indice < len(numeros):
    print(numeros[indice])
    indice += 1
