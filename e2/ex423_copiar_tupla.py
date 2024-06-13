# Ejercicio 423: Crear una copia de un objeto tupla usando notación slicing y la clase tuple.

numeros = (1, 2, 3, 4, 5)

print(numeros)

print()

# Slicing:
numeros_copia_1 = numeros[:]
print(numeros_copia_1)
print(numeros_copia_1 is numeros)

print()

# Clase tuple:

numeros_copia_2 = tuple(numeros)
print(numeros_copia_2)
print(numeros_copia_2 is numeros)
