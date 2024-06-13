# Ejercicio 1090: HackerRank Evaluar un polinommia dada una variable x y una constante k.

# Task

# You are given a polynomial  of a single indeterminate (or variable), .
# You are also given the values of  and . Your task is to verify if .

if __name__ == '__main__':
    x, k = tuple(map(int, input().split()))
    
    p = input()
    
    result = eval(p)
    
    print(result == k)
