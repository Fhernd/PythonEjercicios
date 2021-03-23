# Ejercicio 1078: HackerRank Imprimir en orden lexicográfico las combinaciones de varios caracteres.

# Task

# You are given a string .
# Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()
    
    k = int(k)
    
    result = []
    
    s = sorted(s)
    
    for r in range(1, k + 1):
        combinations_r = list(combinations(s, r))
        combinations_r = [''.join(c) for c in combinations_r]
        combinations_r = sorted(combinations_r)
        
        result.extend(combinations_r)
    
    for c in result:
        print(c)
