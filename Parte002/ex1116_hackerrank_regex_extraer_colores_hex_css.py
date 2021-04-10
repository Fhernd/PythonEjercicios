# Ejercicio 1116: HackerRank Extraer colores hexadecimales usando una expresión regular (regex).

# You are given  lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

# CSS Code Pattern

# ...

import re

if __name__ == '__main__':
    n = int(input())
    
    lines = [input() for _ in range(n)]
    css = '\n'.join(lines)
    
    patron = r'(?!^)#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})'
    
    resultado = re.findall(patron, css, re.MULTILINE)
    
    for r in resultado:
        print(f'#{r}')
