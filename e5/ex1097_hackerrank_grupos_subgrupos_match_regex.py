# Ejercicio 1097: HackerRank Reconocimiento de grupos y subgrupos con un patrón de expresión regular.

# Task

# You are given a string .

# Your task is to find the first occurrence of an alphanumeric character in  (read from left to right)
# that has consecutive repetitions.

import re

if __name__ == '__main__':
    s = input()
    
    pattern = r'([0-9]|[a-z]|[A-Z])\1'
    
    m = re.search(pattern, s)
    
    if m:
        print(m.group()[0])
    else:
        print(-1)
