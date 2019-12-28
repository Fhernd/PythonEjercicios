# Ejercicio 479: Leer el contenido de un objeto array desde un archivo binario con fromfile().

from array import array

with open('Parte001/numeros_array.bin', 'rb') as f:
    numeros = array('i')
    numeros.fromfile(f, 8)

if numeros is not None:
    print(len(numeros))
    print(numeros)
