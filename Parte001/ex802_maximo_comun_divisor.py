# Ejercicio 802: Crear una función para calcular el máximo común divisor (MCD).

from math import floor

def mcd(x, y):
    if x < y:
        return mcd(y, x)
    
    while y != 0:
        x, y = y, x % y

    return x

print(mcd(3, 2))
print(mcd(8, 4))
print(mcd(150, 304))
print(mcd(13, 17))
print(mcd(19, 29))
print(mcd(1000, 10))
