# Ejercicio 481: Agregar múltiples elementos al final de un objeto array con extend().

from array import array

primos = array('d', [1.1, 2.2, 3.3, 5.5])

print(len(primos))
print(primos)

numeros = array('d', [6.6, 7.7, 8.8, 9.9])

print(len(numeros))
print(numeros)

print()

primos.extend(numeros)
print(len(primos))
print(primos)
