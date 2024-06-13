# Ejercicio 1104: Calcular el producto interno y externo entre dos arreglos NumPy.

# Task

# You are given two arrays:  and .
# Your task is to compute their inner and outer product.

# ...

import numpy as np

if __name__ == '__main__':
    data = tuple(map(int, input().split()))
    a = np.array(data)
    
    data = tuple(map(int, input().split()))
    b = np.array(data)
    
    print(np.inner(a, b))
    print(np.outer(a, b))
