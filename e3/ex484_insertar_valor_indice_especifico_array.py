# Ejercicio 484: Agregar un elemento en un índice específico de un objeto array con insert().

from array import array

primos = array('i', [2, 5, 7, 11, 13])

print(len(primos))
print(primos)

print()

primos.insert(1, 3)
print(len(primos))
print(primos)
