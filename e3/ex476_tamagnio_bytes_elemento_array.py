# Ejercicio 476: Obtener el tamaño en bytes de cada elemento de un objeto array con itemsize.

from array import array

numeros = array('i', [2, 3, 5, 7, 11])
print(numeros)
print(numeros.itemsize)

print()

punto_flotante = array('d', [2.2, 3.3, 5.5])
print(punto_flotante)
print(punto_flotante.itemsize)
