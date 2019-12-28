# Ejercicio 451: Crear una copia de todos los elementos de un objeto conjunto.

numeros = set([2, 3, 5, 7])
print(numeros)

numeros_copia = numeros.copy()
print(numeros_copia)

print(numeros_copia is numeros)
