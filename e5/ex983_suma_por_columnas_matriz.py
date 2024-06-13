# Ejercicio 983: Calcular la suma de cada una de las columnas de una matriz.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

suma = []

# [12, 15, 18]

for j in range(len(matriz[0])):
    suma_columna = 0
    for i in range(len(matriz)):
        suma_columna += matriz[i][j]

    suma.append(suma_columna)

print(suma)
