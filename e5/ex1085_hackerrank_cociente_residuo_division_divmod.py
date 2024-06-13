# Ejercicio 1085: HackerRank Función divmod() para obtener el cociente y residuo de una división.

# Task
# Read in two integers,  and , and print three lines.
# The first line is the integer division  (While using Python2 remember to import division from __future__).
# The second line is the result of the modulo operator: .
# The third line prints the divmod of  and .

# ...

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    result = divmod(a, b)
    quotient, reminder = result
    
    print(quotient)
    print(reminder)
    print(result)
