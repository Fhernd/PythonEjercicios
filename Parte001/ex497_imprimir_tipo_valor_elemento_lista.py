# Ejercicio 497: Imprimir el valor y el tipo de dato de cada elemento de una lista.

lista_mixta = ['Python', 3.1415, [1, 2, 3], 0, {'a': 1}, (0, 1), set([0, 1, 2]), 5+3j, True, False]

for i in range(len(lista_mixta)):
    print('Valor: {} - Tipo de dato: {}'.format(lista_mixta[i], type(lista_mixta[i])))
