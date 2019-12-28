# Ejercicio 445: Remover un elemento de un conjunto si está disponible con el método discard().

numeros = set([2, 3, 5, 7, 11, 13])

print(len(numeros))
print(numeros)

print()

numeros.discard(7)

print(len(numeros))
print(numeros)

print()

numeros.discard(0)

print(len(numeros))
print(numeros)
