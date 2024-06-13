# Ejercicio 1131: HackerRank Uso de iterables e iteradores para combinaciones índices de letras.

# The itertools module standardizes a core set of fast, memory efficient tools that are useful by 
# themselves or in combination. Together, they form an iterator algebra making it possible to construct 
# specialized tools succinctly and efficiently in pure Python.

# To read more about the functions in this module, check out their


from itertools import combinations

if __name__ == '__main__':
    n = int(input())
    letters = ''.join(input().split(' '))
    k = int(input())
    
    indexes = list(range(1, len(letters) + 1))
    total = 0
    indexes_chars = list(range(1, k + 1))
    
    combinaciones = list(combinations(indexes, k))

    for c in combinaciones:
        for d in c:
            if letters[d - 1] == 'a':
                total += 1
                break
    
    print('{:.3f}'.format(total/len(combinaciones)))

