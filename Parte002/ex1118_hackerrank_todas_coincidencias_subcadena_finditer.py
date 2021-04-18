# Ejercicio 1118: HackerRank Todas las coincidencias de una subcadena en un texto con finditer().

# Task
# You are given a string .
# Your task is to find the indices of the start and end of string  in .

# ...

import re

if __name__ == '__main__':
    s = input()
    k = input()
    
    result = [(c.start(), c.start() + len(k) - 1) for c in re.finditer(f'(?={k})', s)]
    
    if result:
        for c in result:
            print(c)
    else:
        print((-1, -1))
