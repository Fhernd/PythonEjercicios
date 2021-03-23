# Ejercicio 1076: HackerRank Producto cartesiano entre dos listas con la función product.

# Task

# You are given a two lists  and . Your task is to compute their cartesian product X.

# Example

# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
# Note:  and  are sorted lists, and the cartesian product's tuples should be output in sorted order.

# ...

from itertools import product

if __name__ == '__main__':
    a = list(map(int, input().split()))
    
    b = list(map(int, input().split()))
    
    cartesian_product = list(product(a, b))
    
    for c in cartesian_product:
        print(c, end=' ')
