# Ejercicio 1075: HackerRank Validar si un conjunto es superconjunto estricto de otros conjuntos.

# You are given a set  and  other sets.

# Your job is to find whether set  is a strict superset of each of the  sets.

# Print True, if  is a strict superset of each of the  sets. Otherwise, print False.

# A strict superset has at least one element that does not exist in its subset.

# ...

def is_subset(a, s):
    if len(s) > len(a):
        return
    
    return len(s.difference(a)) == 0

def is_strict_superset(a, sets):
    for s in sets:
        if not is_subset(a, s) or not len(a.difference(s)) >= 1:
            return False
    
    return True

if __name__ == '__main__':
    a = set(map(int, input().split()))
    
    n = int(input())
    
    sets = []
    
    for _ in range(n):
        new_set = set(map(int, input().split()))
        
        sets.append(new_set)
    
    print(is_strict_superset(a, sets))
