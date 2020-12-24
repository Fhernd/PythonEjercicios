# Ejercicio 931: Crear un iterador con filterfalse() para obtener los elementos que no cumplen un predicado.

from itertools import filterfalse

# (0, 1, 2, ..., 8, 9)
# n % 2 == 0
# (0, 2, ...)

rango = list(range(10))
print(rango)

print()

resultado = list(filterfalse(lambda n: n % 2, rango))
print(resultado)

print()

# Nota: El valor cero (0) es semánticamente equivalente a False

print()

resultado = list(filterfalse(lambda n: n % 2 == 0, rango))
print(resultado)
