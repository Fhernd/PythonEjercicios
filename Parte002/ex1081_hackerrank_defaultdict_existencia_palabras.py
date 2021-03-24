# Ejercicio 1081: HackerRank Usar defaultdict para validar la existencia de palabras de diferentes grupos.

# In this challenge, you will be given  integers,  and . There are  words, which might repeat, in word group . 
# There are  words belonging to word group . For each  words, check whether the word has appeared in group  or not. 
# Print the indices of each occurrence of  in group . If it does not appear, print .

# ...

from collections import defaultdict

def check_words_positions(groups):
    b = groups['B']
    
    for w in b:
        if w in groups['A']:
            for i, p in enumerate(groups['A']):
                if w == p:
                    print(i + 1, end=' ')
        else:
            print(-1, end=' ')
        print()

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    
    groups = defaultdict(list)
    
    for _ in range(n):
        groups['A'].append(input())
    
    for _ in range(m):
        groups['B'].append(input())
    
    check_words_positions(groups)
