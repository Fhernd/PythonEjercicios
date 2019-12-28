# Ejercicio 278: Mecanismos para clonar o copiar todos los elementos de una lista.

# list:

numeros = [2, 3, 5, 7, 11]

numeros_copia = list(numeros)

print(numeros)
print(numeros_copia)
print(numeros_copia is numeros)

numeros_2 = numeros

print(numeros_2 is numeros)

print()

# slicing:

numeros_copia = numeros[:]

print(numeros_copia)
print(numeros_copia is numeros)

print()

# Lista de comprensión:
numeros_copia = [numero for numero in numeros]
print(numeros_copia)
print(numeros_copia is numeros)
