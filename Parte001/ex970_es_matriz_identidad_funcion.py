# Ejercicio 970: Definir una función para validar si una matriz dada es identidad.

# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

def es_matriz_identidad(matriz):
    if not isinstance(matriz, list):
        raise TypeError('El argumento debe ser una lista.')

    if len(matriz) != len(matriz[0]):
        raise Exception('La matriz debe ser cuadrada.')

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j and matriz[i][j] != 1:
                return False
            elif i != j and matriz[i][j] != 0:
                return False
        
    return True

datos = [
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

print(es_matriz_identidad(datos))   # True

print()

datos[0][2] = 20

print(es_matriz_identidad(datos))   # False
