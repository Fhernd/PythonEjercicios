# Ejercicio 1112: HackerRank Operaciones ariméticas esenciales sobre arreglos de tipo NumPy.

# Task

# You are given two integer arrays,  and  of dimensions X.
# Your task is to perform the following operations:

# Add ( + )
# Subtract ( - )
# Multiply ( * )
# Integer Division ( / )
# Mod ( % )
# Power ( ** )

# ...

import numpy as np

if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))

    data = [list(map(int, input().split())) for _ in range(n)]
    a = np.array(data)
    
    data = [list(map(int, input().split())) for _ in range(n)]
    b = np.array(data)
    
    print(np.add(a, b))
    print(np.subtract(a, b))
    print(np.multiply(a, b))
    print(a // b)
    print(a % b)
    print(a ** b)
