# Ejercicio 320: Unir o concatenar dos listas por medio del operador suma sobrecargado.

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

# +

lista_3 = lista_1 + lista_2

print(lista_1)
print(lista_2)
print(lista_3) # [1, 2, 3, 4, 5, 6]

print()

lista_4 = lista_2 + lista_1
print(lista_4) # [4, 5, 6, 1, 2, 3]
