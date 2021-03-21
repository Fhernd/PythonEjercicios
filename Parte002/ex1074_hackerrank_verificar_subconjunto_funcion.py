# Ejercicio 1074: HackerRank Determianr si un conjunto A es subconjunto de un conjunto B.

# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .

# If set  is subset of set , print True.
# If set  is not a subset of set , print False.

# ...

def is_subset(a, b):
    if len(a) > len(b):
        return False
    
    return len(a.difference(b)) == 0

if __name__ == '__main__':
    t = int(input())
    
    sets = []
    
    for i in range(t):
        m = int(input())
        a = set(map(int, input().split()))
        
        n = int(input())
        b = set(map(int, input().split()))
        
        sets.append((a, b))
    
    for s in sets:
        print(is_subset(s[0], s[1]))
