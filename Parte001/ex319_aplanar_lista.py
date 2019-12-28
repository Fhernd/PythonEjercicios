# Ejercicio 319: Aplanar una lista de listas por medio de la función itertools.chain().

# [[1, 2, 3], [4, 5], [6, 7, 8], [9]] => [1, 2, 3, 4, 5, 6, 7, 8, 9]

from itertools import chain

lista = [[1, 2, 3], [4, 5], [6, 7, 8], [9]]

lista_aplanada = list(chain(*lista))

print(lista)
print(lista_aplanada)
