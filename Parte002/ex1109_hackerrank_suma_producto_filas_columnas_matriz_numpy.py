# Ejercicio 1109: HackerRank Calcular la suma y producto por filas y columnas de una matriz NumPy.

# Task

# You are given a 2-D array with dimensions X.
# Your task is to perform the  tool over axis  and then find the  of that result.

# ...

import numpy as np

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    
    data = [tuple(map(int, input().split())) for _ in range(n)]
    
    matrix = np.array(data)
    
    sum_per_rows = np.sum(matrix, axis=0)
    product = np.prod(sum_per_rows)
    
    print(product)
