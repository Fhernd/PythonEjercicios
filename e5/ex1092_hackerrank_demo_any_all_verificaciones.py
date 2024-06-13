# Ejercicio 1092: HackerRank Demostración de las funciones any() y all() para verificaciones de datos.

# Task

# You are given a space separated list of integers. If all the integers are positive, then you need to 
# check if any integer is a palindromic integer.

# ...

if __name__ == '__main__':
    n = int(input())
    numbers = tuple(map(int, input().split()))
    
    result = all([n > 0 for n in numbers])
    
    result = any([str(n) == str(n)[::-1] for n in numbers]) and result
    
    print(result)
