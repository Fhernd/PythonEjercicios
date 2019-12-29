# Ejercicio 485: Eliminar un elemento en un índice específico de un objeto array con pop().

from array import array

numeros = array('i', [2, 3, 5, 7, 11])

print(len(numeros))
print(numeros)

print()

numeros.pop()
print(len(numeros))
print(numeros)

print()

numeros.pop(1)
print(len(numeros))
print(numeros)
