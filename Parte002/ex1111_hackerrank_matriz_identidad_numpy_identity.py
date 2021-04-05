# Ejercicio 1111: HackerRank Crear una matriz identidad con la función identity de NumPy.

# Task

# Your task is to print an array of size X with its main diagonal elements as 's and 's everywhere else.

# ...

import numpy as np

np.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))

    matrix = np.eye(n, m, k=0)
    
    print(matrix)
