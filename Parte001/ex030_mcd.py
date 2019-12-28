# Ejercicio 30: Calcular el máximo común divisor de dos números.

# MCD: El número más grande que divide dos números.

def mcd(x, y):
    mcd = 1

    if x % y == 0:
        return y
    
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
    
    return mcd


print(mcd(8, 4))
print(mcd(13, 7))
print(mcd(29, 19))
print(mcd(17, 12))
print(mcd(4, 2))
