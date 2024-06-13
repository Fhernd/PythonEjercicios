# Ejercicio 1038: HackerRank Calcular la división entera y real de dos números, y mostrar resultados.

# URL problema: https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=false

# Task
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

# Example


# The result of the integer division .
# The result of the float division is .
# Print:

# 0
# 0.6

# ...

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    integer_division = a // b
    real_division = a / b
    
    print(integer_division)
    print(real_division)

