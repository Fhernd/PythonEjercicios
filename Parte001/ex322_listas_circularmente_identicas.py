# Ejercicio 322: Comprobar si dos listas son circularmente idénticas usando map() y join().

# [10 10 10 0 0] * 2 = [10 10 10 0 0 0 10 10 10 0 0 0]

def listas_circularmente_identicas(lista_1, lista_2):
    return ' '.join(map(str, lista_2)) in ' '.join(map(str, lista_1 * 2))


lista_1 = [10, 10, 0, 0, 10]
lista_2 = [10, 10, 10, 0, 0]

print(listas_circularmente_identicas(lista_1, lista_2))

lista_3 = [3, 10, 10, 0, 0]
print(listas_circularmente_identicas(lista_1, lista_3))
