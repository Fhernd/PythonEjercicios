# Ejercicio 1039: HackerRank Generar el cuadrado de los números en el rango de 0 hasta n

# Task
# The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

# Example

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

# 0
# 1
# 4

# ...

if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)

