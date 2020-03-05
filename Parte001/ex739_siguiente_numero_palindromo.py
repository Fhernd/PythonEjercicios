# Ejercicio 739: Crear una función para encontrar el siguiente número palíndromo (capicúa).

# 191, 11, 1991, 1001, ...

# n = 191, 202
# n = 11, 22

import sys

def siguiente_palindromo(n):
    """
    Encuentra el siguiente número palíndromo (o capicúa).
    """
    for i in range(n + 1, sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
    
if __name__ == "__main__":
    print(siguiente_palindromo(191))
    print(siguiente_palindromo(11))
    print(siguiente_palindromo(1991))
    print(siguiente_palindromo(1001))
