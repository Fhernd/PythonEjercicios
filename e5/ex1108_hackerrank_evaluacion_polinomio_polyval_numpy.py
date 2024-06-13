# Ejercicio 1108: HackerRank Calcular el valor de un polinomio evaluado en un valor x específico.

# Task

# You are given the coefficients of a polynomial .
# Your task is to find the value of  at point .

# ...

import numpy as np

if __name__ == '__main__':
    coefficients = list(map(float, input().split()))
    
    x = int(input())
    
    y = np.polyval(coefficients, x)
    
    print(y)
