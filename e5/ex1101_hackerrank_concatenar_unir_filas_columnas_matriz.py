# Ejercicio 1101: HackerRank Función concatenate() para unir filas o columnas de varias matrices.

# Task

# You are given two integer arrays of size X and X ( &  are rows, and  is the column).
# Your task is to concatenate the arrays along axis .

# ...

import numpy as np

if __name__ == '__main__':
    n, m, p = tuple(map(int, input().split()))
    
    matrix_1 = []
    matrix_2 = []
    
    for _ in range(n):
        matrix_1.append(list(map(int, input().split())))
    
    for _ in range(m):
        matrix_2.append(list(map(int, input().split())))
    
    matrix_3 = np.concatenate((matrix_1, matrix_2))
    print(matrix_3)
