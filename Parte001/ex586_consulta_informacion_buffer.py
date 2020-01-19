# Ejercicio 586: Consultar la información de búfer de un objeto array con buffer_info().

from array import array

numeros = array('i', [2, 3, 5, 7, 11])

print(numeros.buffer_info())
