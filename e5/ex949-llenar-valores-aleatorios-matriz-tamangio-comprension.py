# Ejercicio 949: Llenar una matriz de nxn con valores aleatorios en el rango 1 a 100 usando una lista de comprensión.

from random import randint

def llenar_matriz(n):
    return [[randint(1, 100) for j in range(n)] for i in range(n)]

resultado = llenar_matriz(5)

print(resultado)
