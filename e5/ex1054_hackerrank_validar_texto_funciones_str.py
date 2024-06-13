# Ejercicio 1054: HackerRank Validar texto con las funciones islower, isalpha, isupper, isdigit, isalnum.

# Task

# You are given a string .
# Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

# Input Format

# A single line containing a string .

# ...

def validate_string(string, fn):
    return any([fn(c) for c in string])

if __name__ == '__main__':
    s = input()
    
    fns = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    
    for fn in fns:
        print(validate_string(s, fn))

