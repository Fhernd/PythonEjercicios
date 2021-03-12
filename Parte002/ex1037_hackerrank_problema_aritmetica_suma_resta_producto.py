# Ejercicio 1037: Dados dos números enteros calcular la suma, resta y producto, y mostrar los resultados.

# URL problema https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example


# Print the following:

# 8
# -2
# 15

# ...

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    addition = a + b
    difference = a - b
    product = a * b
    
    print(addition)
    print(difference)
    print(product)

