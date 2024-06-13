# Ejercicio 473: Agregar elementos a un objeto array con el método de instancia append().

from array import array

numeros = array('i')

print(len(numeros))
print(numeros)

print()

numeros.append(2)
numeros.append(3)
numeros.append(5)
numeros.append(7)

print(len(numeros))
print(numeros)

print()

print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
