# Ejercicio 588: Convertir un objeto array a una lista usando el método tolist().

from array import array

primos = array('i', [2, 3, 5, 7, 11, 13, 17, 19])

print(primos)
print(len(primos))
print(type(primos))

print()

lista_primos = primos.tolist()
print(lista_primos)
print(len(lista_primos))
print(type(lista_primos))
