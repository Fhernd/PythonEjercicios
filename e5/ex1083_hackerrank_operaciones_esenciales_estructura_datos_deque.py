# Ejercicio 1083: HackerRank Realizar operaciones esenciales sobre un objeto deque (estructura de datos).

# Task

# Perform append, pop, popleft and appendleft methods on an empty deque .

# Input Format

# The first line contains an integer , the number of operations.
# The next  lines contains the space separated names of methods and their values.

# ...

from collections import deque

def execute_methods(methods):
    d = deque()
    
    for m in methods:
        method_name = m[0]
        
        if method_name == 'append':
            value = int(m[1])
            d.append(value)
        elif method_name == 'appendleft':
            value = int(m[1])
            d.appendleft(value)
        elif method_name == 'pop':
            if len(d):
                d.pop()
        elif method_name == 'popleft':
            if len(d):
                d.popleft()
        elif method_name == 'clear':
            d.popleft()
    
    return d

if __name__ == '__main__':
    n = int(input())
    
    methods = []
    
    for _ in range(n):
        methods.append(input().split())
    
    result = execute_methods(methods)
    
    for v in result:
        print(v, end=' ')
