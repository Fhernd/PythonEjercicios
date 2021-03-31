# Ejercicio 1099: HackerRank Modificar la forma de un arreglo con la propiedad shape y la función reshape().

# Task

# You are given a space separated list of nine integers. Your task is to convert this list 
# into a X NumPy array.

# ...

import numpy as np

if __name__ == '__main__':
    lista_numeros = list(map(int, input().split()))

    arreglo_numeros = np.array(lista_numeros)

    arreglo_numeros.shape = (3, 3)
    print(arreglo_numeros)
