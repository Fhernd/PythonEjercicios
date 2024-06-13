# Ejercicio 1106: HackerRank NumPy para calcular el promedio, varianza, y desviación estándar.

# Task

# You are given a 2-D array of size X.
# Your task is to find:

# The mean along axis 
# The var along axis 
# The std along axis 

import numpy as np

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    
    matrix = []
    
    for _ in range(n):
        matrix.append(tuple(map(int, input().split())))
    
    matrix = np.array(matrix)
    
    mean = np.mean(matrix, axis=1)
    variance = np.var(matrix, axis=0)
    standard_deviation = np.std(matrix, axis=None)
    
    print(mean)
    print(variance)
    print(round(standard_deviation, 11))
