# Ejercicio 162: Determinar si la suma de los elementos de una lista es igual a un número dado.


def suma_igual(numero, numeros):
    return sum(numeros) == numero


lista_1 = [2, 3, 5, 7, 11]
lista_2 = (8, 9, 2)
lista_3 = [0, 1, 3, 5]

total = 19

print(suma_igual(total, lista_1))
print(suma_igual(total, lista_2))
print(suma_igual(total, lista_3))
