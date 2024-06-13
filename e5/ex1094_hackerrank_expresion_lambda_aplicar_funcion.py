# Ejercicio 1094: HackerRank Usar una expresión lambda para aplicar una función sobre un dato.

# Concept

# The map() function applies a function to every member of an iterable and returns the result. It takes two 
# parameters: first, the function that is to be applied and secondly, the iterables.
# Let's say you are given a list of names, and you have to print a list that contains the length of each name.

# ...

cube = lambda x: x**3


def fibonacci(n):
    fibonaccis = []
    
    for i in range(n):
        fibonaccis.append(fibonacci_recursive(i))
    
    return fibonaccis


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
        

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
