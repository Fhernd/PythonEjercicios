# Ejercicio 1103: HackerRank Multiplicar dos matrices con la función matmul() de NumPy.

# Task

# You are given two arrays  and . Both have dimensions of X.
# Your task is to compute their matrix product.

# ...

import numpy

if __name__ == '__main__':
    n = int(input())
    
    data = [list(map(int, input().split())) for _ in range(n)]
    a = numpy.array(data)
    
    data = [list(map(int, input().split())) for _ in range(n)]
    b = numpy.array(data)
    
    result = numpy.matmul(a, b)
    
    print(result)
