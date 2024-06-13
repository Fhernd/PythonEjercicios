# Ejercicio 428: Remover un elemento de una tupla usando una lista.

numeros = (2, 3, 5, 7, 11)

numeros_lista = list(numeros)
print(numeros_lista)

numeros_lista.pop(2)
print(numeros_lista)

print()

numeros = tuple(numeros_lista)

print(numeros)
