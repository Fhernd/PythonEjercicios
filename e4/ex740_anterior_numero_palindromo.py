# Ejercicio 740: Crear una función para encontrar el anterior número palíndromo (capicúa).

# 191, 11, 1991, 1001, ...

# n = 191, 181
# n = 11, 9

import sys

def anterior_palindromo(n):
    """
    Encuentra el siguiente número palíndromo (o capicúa).
    """
    for i in range(n - 1, 0, -1):
        if str(i) == str(i)[::-1]:
            return i
    
if __name__ == "__main__":
    print(anterior_palindromo(191)) # 181
    print(anterior_palindromo(11)) # 9
    print(anterior_palindromo(1991)) # 1881
    print(anterior_palindromo(1001)) # 999
