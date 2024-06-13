# Ejercicio 1098: HackerRank Crear arreglos con la librería NumPy a través de la función array().

# You are given a space separated list of numbers.
# Your task is to print a reversed NumPy array with the element type float.

# ...

import numpy

def arrays(arr):
    return numpy.array(arr, float)[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)
