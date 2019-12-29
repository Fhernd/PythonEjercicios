# Ejercicio 487: Convertir un objeto array en un objeto list con el método tolist().

from array import array

numeros = array('i', [2, 3, 5, 7, 11, 13, 17, 19])

print(len(numeros))
print(numeros)

print()

primos = numeros.tolist()
print(len(primos))
print(type(primos))
print(primos)
