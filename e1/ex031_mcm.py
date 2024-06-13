# Ejercicio 31: Calcular el mínimo común múltiplo de dos números.

# MCM: Es el número positivo más pequeño que es múltiplo de dos números.


def mcm(x, y):
    z = max(x, y)

    while True:
        if (z % x == 0) and (z % y == 0):
            return z
        
        z += 1


print(mcm(2, 4))
print(mcm(32, 13))
print(mcm(17, 15))
