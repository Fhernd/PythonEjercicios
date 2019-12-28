# Ejercicio 418: Agregar un nuevo elemento a un objeto tupla.

numeros = (1, 2, 3, 4)

print(len(numeros))
print(numeros)

print()

numeros_nuevo = numeros + (5,)

print(len(numeros_nuevo))
print(numeros_nuevo)

print(numeros is numeros_nuevo)
