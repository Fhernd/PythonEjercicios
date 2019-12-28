# Ejercicio 354: Reemplazar el último elemento de una lista por los elementos de otra lista.

# [1, 2, 3, 4, 5]
# [6, 7, 8]
# => [1, 2, 3, 4, 6, 7, 8]

lista_a = [1, 2, 3, 4, 5]
lista_b = [6, 7, 8]

print(lista_a)
print(lista_b)

print()

lista_a[-1:] = lista_b

print(lista_a)
