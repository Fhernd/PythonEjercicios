# Ejercicio 82: Calcular la suma de los elementos de un objeto iterable.

numeros = [13, 7, 2, 5, 29, 17, 7, 31, 101]

suma = 0

for numero in numeros:
    suma += numero

print('Suma de todos los números: %i' % suma)

print()

suma = sum(numeros)

print('Suma de todos los números: %i' % suma)
