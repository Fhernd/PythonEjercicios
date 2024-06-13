# Ejercicio 1077: HackerRank Generar permutaciones a través de la función permutations().

# Task

# You are given a string .
# Your task is to print all possible permutations of size  of the string in lexicographic sorted order.

# ...

from itertools import permutations

if __name__ == '__main__':
    s, k = input().split()
    k = int(k)
    
    result = list(permutations(s, r=k))
    result = [''.join(p) for p in result]
    result = sorted(result)
        
    for p in result:
        print(p)

