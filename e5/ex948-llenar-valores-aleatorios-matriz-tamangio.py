# Ejercicio 948: Llenar una matriz de nxn con valores aleatorios en el rango 1 a 100.

from random import randint

def llenar_matriz(n):
    matriz = []

    for r in range(n):
        fila = []

        for c in range(n):
            fila.append(randint(1, 100))
        
        matriz.append(fila)
    
    return matriz

resultado = llenar_matriz(5)

print(resultado)
