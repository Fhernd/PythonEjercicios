# Ejercicio 1120: HackerRank Validar con una expresión regular un número de identificación único (UID).

# ABCXYZ company has up to  employees.
# The company decides to create a unique identification number (UID) for each of its employees.
# The company has assigned you the task of validating all the randomly generated UIDs.

# A valid UID must follow the rules below:

# It must contain at least  uppercase English alphabet characters.
# It must contain at least  digits ( - ).
# It should only contain alphanumeric characters ( - ,  -  &  - ).
# No character should repeat.
# There must be exactly  characters in a valid UID.

import re

def is_valid_uid(test_case: str) -> bool:
    pattern = r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:\D*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'
    
    return re.search(pattern, test_case)

if __name__ == '__main__':
    tests = [input() for _ in range(int(input()))]
    
    for t in tests:
        print('Valid' if is_valid_uid(t) else 'Invalid')
