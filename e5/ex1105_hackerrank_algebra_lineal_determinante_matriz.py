# Ejercicio 1105: HackerRank Álgebral lineal con NumPy - Cálculo del determinante de una matriz.

# Task

# You are given a square matrix  with dimensions X. Your task is to find the determinant. 
# Note: Round the answer to 2 places after the decimal.

# ...

import numpy as np

if __name__ == '__main__':
    n = int(input())
    
    data = []
    
    for _ in range(n):
        data.append(tuple(map(float, input().split())))
    
    matrix = np.array(data)
    
    determinant = np.linalg.det(matrix)
    if (determinant == 0):
        print(determinant)
    else:
        print(round(determinant, 2))
