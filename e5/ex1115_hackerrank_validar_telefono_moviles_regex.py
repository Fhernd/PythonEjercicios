# Ejercicio 1115: HackeRank Validar números de teléfono móvil con una expresión regular (regex).

# Concept

# A valid mobile number is a ten digit number starting with a  or .

# Regular expressions are a key concept in any programming language. A quick explanation with Python 
# examples is available here. You could also go through the link below to read more about regular 
# expressions in Python.

# https://developers.google.com/edu/python/regular-expressions

# ...

import re

if __name__ == '__main__':
    phone_numbers = [input() for _ in range(int(input()))]
    
    pattern = '^[789]\d{9}$'
    validator = re.compile(pattern)
    
    for p in phone_numbers:
        print('YES' if validator.search(p) else 'NO')
