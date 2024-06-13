# Ejercicio 420: Convertir un objeto tupla en un objeto lista.

tupla = (1, 2, 3)

print(len(tupla))
print(type(tupla))
print(tupla)

print()

lista = list(tupla)

print(len(lista))
print(type(lista))
print(lista)

print()

lista.append(4)
lista.append(5)
lista.append(6)

print(len(lista))
print(lista)

print()

tupla = tuple(lista)

print(len(tupla))
print(type(tupla))
print(tupla)
