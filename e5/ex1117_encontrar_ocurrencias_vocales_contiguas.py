# Ejercicio 1117: HackerRank Encontrar ocurrencias de dos vocales contiguas con una RegEx.

# Task
# You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-).
# Your task is to find all the substrings of  that contains  or more vowels.
# Also, these substrings must lie in between  consonants and should contain vowels only.

# ...

import re

if __name__ == '__main__':
    s = input()
    
    # raareer
    pattern = r'[^aeiou]([aeiouAEIOU]{2,})(?=[^aeiou])'
    
    result = re.findall(pattern, s, re.MULTILINE)
    
    if len(result):
        for r in result:
            print(r)
    else:
        print(-1)
