# Ejercicio 263: Encontrar el primer carácter repetido de una cadena.

# Solución:

# Python => 0, P; 1, y; ...

def primer_caracter_repetido(cadena):
    for i, c in enumerate(cadena):
        if cadena[i + 1:].count(c) > 0:
            return c
    
    return None


cadena = 'Python es tremendo'

print(primer_caracter_repetido(cadena))

cadena = 'Python'

print(primer_caracter_repetido(cadena))
