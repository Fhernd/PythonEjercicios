# Ejercicio 1107: HackerRank Funciones min() y max() para obtener el mínimo y máximo de una matriz NumPy.

# Task

# You are given a 2-D array with dimensions X.
# Your task is to perform the min function over axis  and then find the max of that.

# ...

import numpy as np

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    
    data = []
    
    for _ in range(n):
        data.append(list(map(int, input().split())))
    
    matrix = np.array(data)
    
    minimum = np.min(matrix, axis=1)
    maximum = np.max(minimum)
    
    print(maximum)
