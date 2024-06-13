# Ejercicio 1100: HackerRank Obtener la transpuesta y la versión aplanada de una matriz NumPy.

# Task

# You are given a X integer array matrix with space separated elements ( = rows and  = columns).
# Your task is to print the transpose and flatten results.

# ...

import numpy as np

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    
    matriz = []
    for _ in range(n):
        matriz.append(list(map(int, input().split())))
    
    matriz = np.array(matriz)
    
    print(np.transpose(matriz))
    print(matriz.flatten())
