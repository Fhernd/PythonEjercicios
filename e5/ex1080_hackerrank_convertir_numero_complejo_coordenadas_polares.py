# Ejercicio 1080: HackerRank Convertir un número complejo a coordenadas polares.

# Task
# You are given a complex . Your task is to convert it to polar coordinates.

# Input Format

# A single line containing the complex number . Note: complex() function can be used in python 
# to convert the input as a complex number.

# ...

import cmath

def convert_complex_polar_coordinates(complex_number):
    r = abs(complex_number)
    phase = cmath.phase(complex_number)
    
    return r, phase

if __name__ == '__main__':
    data = complex(input())
    
    result = convert_complex_polar_coordinates(data)
    
    print(round(result[0], 3))
    print(round(result[1], 3))
