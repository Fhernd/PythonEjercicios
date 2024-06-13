# Ejercicio 1110: HackerRank Usar las funciones floor(), ceil(), y rint() sobre un arreglo NumPy.

# Task
# You are given a 1-D array, . Your task is to print the ,  and  of all the elements of .

# ...

import numpy as np

np.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    values = list(map(float, input().split()))
    
    array = np.array(values)
    
    print(np.floor(array))
    print(np.ceil(array))
    print(np.rint(array))
