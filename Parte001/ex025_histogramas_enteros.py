# Ejercicio 25: Crear un histograma a partir de una lista de enteros.

# Análisis

# [2, 1, 5, 3]
# **
# *
# *****
# ***


def crear_histograma(lista, caracter='*'):
    for e in lista:
        print(caracter * e)



lista = [2, 1, 5, 3]
crear_histograma(lista)
print()
lista = [2, 7, 13, 11, 19]
crear_histograma(lista)
