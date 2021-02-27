# Ejercicio 982: Calcular la suma de cada una de las filas de una matriz.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# [6, 15, 24]

suma_filas = []

for f in matriz:
    suma_filas.append(sum(f))

print(suma_filas) # # [6, 15, 24]
