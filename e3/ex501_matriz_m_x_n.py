# Ejercicio 501: Crear una matriz mxn con los tamaños especificados por el usuario.

def crear_matriz(m, n):
    """
    Crea una matriz de m filas y n columnas.
    """
    return [[i*j for j in range(n)] for i in range(m)]


filas = int(input('Digite la cantidad de filas: '))
columnas = int(input('Digite la cantidad de columnas: '))

matriz = crear_matriz(filas, columnas)

print(matriz)
