# Ejercicio 965: Definir una función personalizada para calcular la suma de dos matrices.

def calcular_suma_matrices(A, B):
    if len(A) != len(B):
        raise Exception('Las dos matrices deben tener la misma cantidad de filas.')

    if len(A[0]) != len(B[0]):
        raise Exception('Las dos matrices deben tener la misma cantidad de columnas.')

    suma_matrices = []

    for i in range(len(A)):
        fila = []
        for j in range(len(A[0])):
            fila.append(A[i][j] + B[i][j])
        
        suma_matrices.append(fila)
    
    return suma_matrices

A = [[1, 2, 3], [4, 5, 6]] # 2x3
B = [[2, 3, 5], [11, 7, 5]] # 2x3

resultado = calcular_suma_matrices(A, B)
print(resultado) # [[3, 5, 8], [15, 12, 11]]

print()

C = [[2, 3], [5, 7], [11, 13]]

try:
    resultado = calcular_suma_matrices(A, C)
    print(resultado)
except Exception as e:
    print(e)
