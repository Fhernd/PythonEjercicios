# Ejercicio 1063: HackerRank Verificar si ciertas cadenas representan expresiones regulares.

# You are given a string .
# Your task is to find out whether  is a valid regex or not.

# Input Format

# The first line contains integer , the number of test cases.
# The next  lines contains the string .

# ...

import re

def validate_strings_for_regex(string):
    try:
        re.compile(string)
        
        return True
    except:
        return False


if __name__ == '__main__':
    t = int(input())
    strings = [input() for _ in range(t)]
    
    for s in strings:
        print(validate_strings_for_regex(s))

