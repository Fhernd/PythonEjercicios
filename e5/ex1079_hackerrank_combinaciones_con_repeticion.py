# Ejercicio 1079: HackerRank Generar combinaciones con repetición utilizando combinations_with_replacement().

# Task

# You are given a string .
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, k = input().split()
    
    k = int(k)
    s = sorted(s)
    
    result = list(combinations_with_replacement(s, k))
    result = [''.join(c) for c in result]
    
    for c in result:
        print(c)
