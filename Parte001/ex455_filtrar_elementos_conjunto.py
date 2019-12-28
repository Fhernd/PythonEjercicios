# Ejercicio 455: Filtrar los elementos de un objeto conjunto con la función filter().

numeros = set([2, 3, 5, 7, 11, 13, 17, 19])

print(len(numeros))
print(numeros)

print()

resultado = set(filter(lambda e: e > 7, numeros))

print(resultado)
