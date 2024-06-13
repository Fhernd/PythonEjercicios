# Ejercicio 478: Guardar los elementos de un objeto array en un archivo binario con tofile().

from array import array

numeros = array('i', [2, 3, 5, 7, 11, 13, 17, 19])

with open('Parte001/numeros_array.bin', 'wb') as f:
    numeros.tofile(f)
