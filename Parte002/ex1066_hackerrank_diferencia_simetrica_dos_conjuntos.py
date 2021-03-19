# Ejercicio 1066: HackerRank Función para calcular la diferencia simétrica entre dos conjuntos.

# Task
# Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

# Input Format

# The first line of input contains an integer, .
# The second line contains  space-separated integers.
# The third line contains an integer, .
# The fourth line contains  space-separated integers.

# ...

def symmetric_difference(m, n):
    result = m.difference(n).union(n.difference(m))
    
    return result

if __name__ == '__main__':
    m = int(input())
    m = set(map(int, input().split()))
    
    n = int(input())
    n = set(map(int, input().split()))
    
    result = symmetric_difference(m, n)
    
    result = sorted(list(result))
    
    for n in result:
        print(n)
